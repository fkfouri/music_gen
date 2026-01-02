import random

from scamp import *

s = Session()
instr = s.new_part("cello")

pitch = 65

while True:
    instr.play_note(pitch, 0.8, 0.25)
    pitch += random.choice([-1, 1])
    # pitch += 1
    # if pitch > 96:
    #     pitch = 55
    print(f"{chr(pitch)}:{pitch}", end=" ")
