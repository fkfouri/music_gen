import mido

from src.merger_midi import _VERSION, main


def _make_track(name: str, note: int, start_tick: int = 0, program: int | None = None) -> mido.MidiTrack:
    track = mido.MidiTrack()
    track.append(mido.MetaMessage("track_name", name=name))
    if program is not None:
        track.append(mido.Message("program_change", program=program))
    track.append(mido.Message("note_on", note=note, velocity=90, time=start_tick))
    track.append(mido.Message("note_off", note=note, velocity=0, time=120))
    track.append(mido.MetaMessage("end_of_track"))
    return track


def _write_midi(path, tracks: list[mido.MidiTrack]) -> None:
    midi = mido.MidiFile()
    midi.tracks.extend(tracks)
    midi.save(path)


def test_main_merges_tracks_of_the_same_instrument_by_default(tmp_path, monkeypatch):
    input_dir = tmp_path / "input"
    input_dir.mkdir()
    _write_midi(
        input_dir / "song.mid",
        [
            _make_track("Piano", 60),
            _make_track("Piano 2", 64, start_tick=120),
            _make_track("", 36),
        ],
    )
    monkeypatch.chdir(tmp_path)

    assert main(["--input-dir", str(input_dir)]) == 0

    result = mido.MidiFile(tmp_path / "merged.mid")
    assert len(result.tracks) == 2
    piano = next(track for track in result.tracks if track.name == "Piano")
    assert [message.note for message in piano if message.type == "note_on"] == [60, 64]

    absolute_ticks = []
    tick = 0
    for message in piano:
        tick += message.time
        if message.type == "note_on":
            absolute_ticks.append(tick)
    assert absolute_ticks == [0, 120]


def test_main_merges_matching_tracks_across_input_files(tmp_path, monkeypatch):
    input_dir = tmp_path / "input"
    input_dir.mkdir()
    _write_midi(input_dir / "a.mid", [_make_track("Piano", 60)])
    _write_midi(input_dir / "b.mid", [_make_track("Piano 2", 64, start_tick=120)])
    monkeypatch.chdir(tmp_path)

    assert main(["--input-dir", str(input_dir)]) == 0

    result = mido.MidiFile(tmp_path / "merged.mid")
    assert len(result.tracks) == 1
    assert [message.note for message in result.tracks[0] if message.type == "note_on"] == [60, 64]


def test_main_removes_duplicate_notes_with_matching_onset_pitch_and_velocity(tmp_path, monkeypatch):
    _write_midi(
        tmp_path / "song.mid",
        [
            _make_track("Fretless Bass", 40, start_tick=120),
            _make_track("Fretless Bass 2", 40, start_tick=120),
            _make_track("Fretless Bass 3", 43, start_tick=240),
        ],
    )
    monkeypatch.chdir(tmp_path)

    assert main([]) == 0

    result = mido.MidiFile(tmp_path / "merged.mid")
    assert len(result.tracks) == 1
    track = result.tracks[0]
    note_ons = [message for message in track if message.type == "note_on" and message.velocity > 0]
    note_offs = [
        message
        for message in track
        if message.type == "note_off" or (message.type == "note_on" and message.velocity == 0)
    ]
    assert [(message.note, message.velocity) for message in note_ons] == [(40, 90), (43, 90)]
    assert len(note_offs) == 2


def test_main_can_keep_duplicate_notes(tmp_path, monkeypatch):
    _write_midi(
        tmp_path / "song.mid",
        [
            _make_track("Fretless Bass", 40, start_tick=120),
            _make_track("Fretless Bass 2", 40, start_tick=120),
        ],
    )
    monkeypatch.chdir(tmp_path)

    assert main(["--no-remove-duplicate-notes"]) == 0

    result = mido.MidiFile(tmp_path / "merged.mid")
    track = result.tracks[0]
    note_ons = [message for message in track if message.type == "note_on" and message.velocity > 0]
    note_offs = [
        message
        for message in track
        if message.type == "note_off" or (message.type == "note_on" and message.velocity == 0)
    ]
    assert len(note_ons) == 2
    assert len(note_offs) == 2


def test_main_keeps_numbered_tracks_with_different_programs_separate(tmp_path, monkeypatch):
    _write_midi(
        tmp_path / "song.mid",
        [
            _make_track("Synth Strings 1", 60, program=50),
            _make_track("Synth Strings 2", 64, program=51),
        ],
    )
    monkeypatch.chdir(tmp_path)

    assert main([]) == 0

    result = mido.MidiFile(tmp_path / "merged.mid")
    assert len(result.tracks) == 2
    assert [track.name for track in result.tracks] == ["Synth Strings 1", "Synth Strings 2"]


def test_main_can_disable_instrument_track_merging(tmp_path, monkeypatch):
    _write_midi(
        tmp_path / "song.mid",
        [_make_track("Piano", 60), _make_track("Piano 2", 64)],
    )
    monkeypatch.chdir(tmp_path)

    assert main(["--no-merge-same-instrument"]) == 0

    result = mido.MidiFile(tmp_path / "merged.mid")
    assert len(result.tracks) == 2
    assert [track.name for track in result.tracks] == ["Piano", "Piano 2"]


def test_help_lists_supported_options(capsys):
    try:
        main(["--help"])
    except SystemExit as error:
        assert error.code == 0
    else:
        raise AssertionError("A opção --help deveria encerrar o programa.")

    help_text = capsys.readouterr().out
    assert "--input-dir" in help_text
    assert "--output" in help_text
    assert "--no-merge-same-instrument" in help_text
    assert "--no-remove-duplicate-notes" in help_text
    assert f"merger_midi {_VERSION}" in help_text


def test_version_option_displays_project_version(capsys):
    try:
        main(["--version"])
    except SystemExit as error:
        assert error.code == 0
    else:
        raise AssertionError("A opção --version deveria encerrar o programa.")

    assert capsys.readouterr().out.strip() == f"merger_midi {_VERSION}"
