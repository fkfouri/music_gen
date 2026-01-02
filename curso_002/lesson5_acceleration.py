from scamp import *

s = Session()
instr = s.new_part("piano")

pitch = 80
pitch_velocity = 0
pitch_acceleration = -98

while True:
    instr.play_note(pitch, 0.7, 0.05)
    pitch_velocity += pitch_acceleration * 0.05
    pitch += pitch_velocity * 0.05
    if pitch < 25:
        pitch_velocity *= -1

    print(f"{chr(int(pitch))}:{pitch}", end=" ")
