import math

from scamp import *
from scamp_extensions.pitch import Scale

s = Session()

scale = Scale.melodic_minor(62)

instr = s.new_part("strings")

while True:
    raw_pitch = 80 + 10 * math.sin(s.beat())
    raw_pitch = 80 + 10 * math.sin(100 / (0.1 + s.beat()))

    pitch = scale.round(raw_pitch)

    instr.play_note(pitch, 0.8, 0.25, "stacatto")

    print(f"{raw_pitch}:{pitch}", end=" ")
