from scamp import *
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


while True:
    # organ.play_note(build_chord([0,2,4,5,7,9,11], 3, 60, True), 0.8, 0.25)
    pitch = build_chord(
        [5, 7],
        random.randint(3, 8),
        60,
    )
    # instr.play_chord(pitch, 0.8, 2)
    instr.play_chord(pitch, 0.8, random.randrange(1, 16) * .25, "stacatto")
