from mido import MidiFile
from mido.midifiles import meta as mido_meta
import mido.midifiles.midifiles as mido_midifiles
from pathlib import Path

# Monkey-patch: converte meta messages inválidas em UnknownMetaMessage
# Precisa patchear em ambos os módulos pois midifiles.py importa diretamente
_original_build = mido_meta.build_meta_message

def _safe_build_meta_message(meta_type, data, delta=0):
    try:
        return _original_build(meta_type, data, delta)
    except Exception:
        return mido_meta.UnknownMetaMessage(meta_type, data, time=delta)

mido_meta.build_meta_message = _safe_build_meta_message
mido_midifiles.build_meta_message = _safe_build_meta_message

arquivos = sorted(Path('.').glob('*.mid'))

novo = MidiFile()

for arq in arquivos:
    try:
        mid = MidiFile(arq, clip=True)
        for track in mid.tracks:
            novo.tracks.append(track)
    except Exception as e:
        print(f"Aviso: ignorando '{arq}' — {e}")

novo.save('merged.mid')