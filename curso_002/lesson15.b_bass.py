from scamp import *
import random
from itertools import cycle

s = Session(tempo=100)

# bass = s.new_midi_part("slap bass", "IAC Bus 1", start_channel=3, num_channels=1)

bass_pitches = [38, 50, 43, 44, 45, 48, 60, 41, 40, 39, 61]
bass_columes = [0.8, 1, 0.3, 0.8, 0.8, 0.3, 1, 0.3, 0.8, 0.8, 1]
bass_durs = [0.75, 0.25, 0.25, 0.5, 0.5, 0.25, 0.5, 0.25, 0.5, 0.5, 0.25]

# drums = s.new_part("drums")
# theramin = s.new_part("theramin")
bass = s.new_part("slap bass")

while True:
    for pitch, volume, dur in zip(
        cycle(bass_pitches), cycle(bass_columes), cycle(bass_durs)
    ):  # for pitch,volume,dur in zip(bass_pitches,bass_columes,bass_durs):
        bass.play_note(pitch, volume, dur)
