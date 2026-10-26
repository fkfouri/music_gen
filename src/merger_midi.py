import argparse
import re
import sys
from collections import defaultdict
from pathlib import Path

import mido
import mido.midifiles.midifiles as mido_midifiles
from mido import MidiFile, MidiTrack
from mido.midifiles import meta as mido_meta

_original_build = mido_meta.build_meta_message


def _safe_build_meta_message(meta_type, data, delta=0):
    try:
        return _original_build(meta_type, data, delta)
    except Exception:
        return mido_meta.UnknownMetaMessage(meta_type, data, time=delta)


mido_meta.build_meta_message = _safe_build_meta_message
mido_midifiles.build_meta_message = _safe_build_meta_message

_TRACK_NUMBER_SUFFIX = re.compile(r"[\s._-]*\(?\d+\)?$")


def _read_project_version() -> str:
    if getattr(sys, "frozen", False):
        project_file = Path(sys._MEIPASS) / "pyproject.toml"
    else:
        project_file = Path(__file__).resolve().parents[1] / "pyproject.toml"

    in_project_section = False
    for line in project_file.read_text(encoding="utf-8").splitlines():
        section = line.strip()
        if section.startswith("["):
            in_project_section = section == "[project]"
        elif in_project_section:
            match = re.match(r'^version\s*=\s*"([^"]+)"\s*$', line.strip())
            if match:
                return match.group(1)

    raise ValueError(f"Versão não encontrada em [project] no arquivo {project_file}")


_VERSION = _read_project_version()


def _normalize_track_name(name: str) -> str:
    return _TRACK_NUMBER_SUFFIX.sub("", name.strip().casefold()).strip()


def _programs(track: MidiTrack) -> frozenset[int]:
    return frozenset(message.program for message in track if message.type == "program_change")


def _deduplicate_note_events(events):
    active_notes = defaultdict(list)
    note_pairs = []

    for tick, track_index, order, message in sorted(events, key=lambda event: (event[1], event[2])):
        if message.type not in {"note_on", "note_off"}:
            continue

        key = (track_index, message.channel, message.note)
        if message.type == "note_on" and message.velocity > 0:
            active_notes[key].append((tick, order, message.velocity))
        elif message.type == "note_off" or (message.type == "note_on" and message.velocity == 0):
            if active_notes[key]:
                start_tick, start_order, velocity = active_notes[key].pop(0)
                note_pairs.append(
                    (
                        (message.channel, message.note, start_tick, velocity),
                        (track_index, start_order),
                        (track_index, order),
                    )
                )

    note_pairs.sort(key=lambda pair: (pair[0][2], pair[1][0], pair[1][1]))
    seen_notes = set()
    duplicate_events = set()
    for signature, note_on, note_off in note_pairs:
        if signature in seen_notes:
            duplicate_events.add(note_on)
            duplicate_events.add(note_off)
        else:
            seen_notes.add(signature)

    return [
        event
        for event in events
        if (event[1], event[2]) not in duplicate_events
    ]


def merge_same_instrument_tracks(midi: MidiFile, remove_duplicate_notes: bool = True) -> list[MidiTrack]:
    """Consolida trilhas nomeadas equivalentes, preservando trilhas sem nome."""
    groups = defaultdict(list)
    independent_tracks = []

    for index, track in enumerate(midi.tracks):
        name = track.name.strip()
        if not name:
            independent_tracks.append((index, track))
            continue
        groups[_normalize_track_name(name)].append((index, track))

    entries = [(index, None, track) for index, track in independent_tracks]
    for instrument, tracks in groups.items():
        program_profiles = {_programs(track) for _, track in tracks}
        configured_profiles = {profile for profile in program_profiles if profile}
        if len(configured_profiles) > 1:
            by_program = defaultdict(list)
            for item in tracks:
                by_program[_programs(item[1])].append(item)
            track_groups = by_program.values()
        else:
            track_groups = [tracks]

        for track_group in track_groups:
            entries.append((track_group[0][0], instrument, track_group))
    entries.sort(key=lambda entry: entry[0])

    result = []
    for _, instrument, payload in entries:
        if instrument is None or len(payload) == 1:
            result.append(payload if instrument is None else payload[0][1])
            continue

        events = []
        end_tick = 0
        for track_index, track in payload:
            absolute_tick = 0
            for order, message in enumerate(track):
                absolute_tick += message.time
                end_tick = max(end_tick, absolute_tick)

                if message.is_meta and message.type in {"track_name", "end_of_track"}:
                    continue
                events.append((absolute_tick, track_index, order, message.copy(time=0)))

        if remove_duplicate_notes:
            events = _deduplicate_note_events(events)
        events.sort(key=lambda event: event[:3])
        merged = MidiTrack()
        track_names = [track.name.strip() for _, track in payload]
        merged.name = next(
            (name for name in track_names if _normalize_track_name(name) == name.casefold()),
            track_names[0],
        )

        previous_tick = 0
        for tick, _, _, message in events:
            message.time = tick - previous_tick
            merged.append(message)
            previous_tick = tick
        merged.append(mido.MetaMessage("end_of_track", time=end_tick - previous_tick))
        result.append(merged)

    return result


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            f"merger_midi {_VERSION} — junta arquivos MIDI e, por padrão, "
            "consolida trilhas do mesmo instrumento."
        ),
        epilog=(
            "Exemplo: merger_midi.exe --input-dir midi_entrada --output resultado.mid "
            "--no-merge-same-instrument"
        ),
    )
    parser.add_argument("--version", action="version", version=f"merger_midi {_VERSION}")
    parser.add_argument(
        "--input-dir",
        type=Path,
        default=Path("."),
        help="pasta com os arquivos .mid (padrão: pasta atual)",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("merged.mid"),
        help="caminho do MIDI resultante (padrão: merged.mid)",
    )
    parser.add_argument(
        "--no-merge-same-instrument",
        action="store_false",
        dest="merge_same_instrument",
        help="mantém as trilhas separadas, sem consolidar instrumentos repetidos",
    )
    parser.add_argument(
        "--no-remove-duplicate-notes",
        action="store_false",
        dest="remove_duplicate_notes",
        help="mantém notas idênticas que começam no mesmo tempo, altura e velocidade",
    )
    parser.set_defaults(merge_same_instrument=True)
    parser.set_defaults(remove_duplicate_notes=True)
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    if not args.input_dir.is_dir():
        raise SystemExit(f"A pasta de entrada não existe: {args.input_dir}")

    input_files = sorted(args.input_dir.glob("*.mid"))
    output_path = args.output.resolve()
    novo = MidiFile()
    tracks_before = 0

    for arq in input_files:
        if arq.resolve() == output_path:
            continue
        try:
            mid = MidiFile(arq, clip=True)
            tracks_before += len(mid.tracks)
            novo.tracks.extend(mid.tracks)
        except Exception as error:
            print(f"Aviso: ignorando '{arq}' — {error}")

    if args.merge_same_instrument:
        novo.tracks = merge_same_instrument_tracks(novo, remove_duplicate_notes=args.remove_duplicate_notes)

    novo.save(args.output)
    print(
        f"Arquivos encontrados: {len(input_files)}; "
        f"trilhas originais: {tracks_before}; "
        f"trilhas resultantes: {len(novo.tracks)}; "
        f"arquivo de saída: {args.output}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
