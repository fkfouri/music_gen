from scamp import *
from scamp_extensions.pitch import Scale

s = Session()
s.tempo = 120
instr = s.new_part("violin")

scale = Scale.natural_minor(62)  # D minor
scale = Scale.major(60)  # C major

print(list(scale))

while True:
    for n in range(3):
        for m in range(3):
            for l in range(3):
                for k in range(3):
                    pitch = scale[k + l + m + n]
                    instr.play_note(pitch, 0.8, 0.25)
                    print(f"{chr(int(pitch))}:{pitch}", end=" ")
