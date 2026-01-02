import math

from scamp import *
from scamp_extensions.pitch import Scale

s = Session()

scale = Scale.melodic_minor(62)

instr = s.new_part("strings")

s.start_transcribing()

i = 0
while True:
    raw_pitch = 80 + 10 * math.sin(s.beat())
    raw_pitch = 80 + 10 * math.sin(100 / (0.1 + s.beat()))

    pitch = scale.round(raw_pitch)

    instr.play_note(pitch, 0.8, 0.25)

    print(f"{raw_pitch}:{pitch}", end=" ")

    i += 1
    if i > 30:
        break

s.wait(1)
s

performance = s.stop_transcribing()
# performance.to_score(
#     QuantizationScheme.from_time_signature("3/4", 16),
#     title="Teste Kfouri",
#     composer="Last Nobler",
# ).show()

# performance.to_midi("test.mid")
performance.export_to_midi_file("./music/scamp_test.mid")
