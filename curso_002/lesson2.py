import random

from scamp import *

s = Session()
instr = s.new_part("cello")

pitch = 55

while True:
    instr.play_note(pitch, 0.8, 0.25)
    pitch += random.choice([-1, 1, 2, -2])
    # pitch += 1
    # if pitch > 96:
    #     pitch = 55
    print(pitch, end=" ")

text = "Dante Kfouri"
text += " 2024!"

for char in text:
    if char == " ":
        wait(0.2)
    elif char.isalnum():
        instr.play_note(ord(char) - 20, 0.5, 0.06)
    else:
        wait(0.2)
        instr.play_note(ord(char), 0.8, 0.06)
        wait(0.2)
