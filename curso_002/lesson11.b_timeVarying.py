from scamp import *
from scamp_extensions.utilities import TimeVaryingParameter
import random


def build_chord(interval_options, num_notes, pitch_center, round_transposition=True):

    chord = [0]

    while len(chord) < num_notes:
        chord.append(chord[-1] + random.choice(interval_options))

    trasposition = pitch_center - sum(chord) / len(chord)

    if round_transposition:
        trasposition = round(trasposition)

    return [pitch + trasposition for pitch in chord]


s = Session()
instr = s.new_part("church organ")

INTERVAL_OPTIONS = [2, 5, 10]
# 4 notas por 30 tempos, depois para para 1 nota por 30 tempos, depois para para 10 notas por 40 tempos
NUM_NOTES_IN_CHORD = TimeVaryingParameter([4, 1, 1, 10], [30, 30, 40])
PITCH_CENTER = TimeVaryingParameter([60, 90, 40], [50, 50])
VOLUME = 0.9
DURATION = TimeVaryingParameter([0.25, 0.005, 2], [70, 30])
STACATTO_CHANCE = TimeVaryingParameter([1, 0.5, 1, 0], [30, 30, 40])

while True:
    # organ.play_note(build_chord([0,2,4,5,7,9,11], 3, 60, True), 0.8, 0.25)
    pitch = build_chord(INTERVAL_OPTIONS, NUM_NOTES_IN_CHORD(), PITCH_CENTER())
    instr.play_chord(
        pitch,
        VOLUME,
        DURATION(),
        "stacatto" if random.random() < STACATTO_CHANCE() else None,
    )
    # instr.play_chord(pitch, 0.8, random.randrange(1, 16) * .25, "stacatto")
