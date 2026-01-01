# Generating radom melodies

from __init__ import __MUSIC_PATH__

import numpy as np
from mido import Message, MidiFile, MidiTrack

# define our variables
num_notes = 16  # number of notes in the melody
note_range = (60, 72)  # MIDI note numbers for C4 to C5
velocity = 64
tempo = 500


# scale = [60, 62, 64, 65, 67, 69, 71, 72]  # C major scale
# num_notes = 50  # number of notes in the melody
# tempo = 120  # bpm
# duration = 1.0  # duration of each note in seconds
# volume = 100  # volume of each note



# Generate random melody
notes = np.random.randint(note_range[0], note_range[1] + 1, num_notes)


# Create MIDI file and track
mid = MidiFile()
track = MidiTrack()
mid.tracks.append(track)

for note in notes:
    track.append(Message('note_on', note=note, velocity=velocity, time=0))
    track.append(Message('note_off', note=note, velocity=velocity, time=tempo)) 


output_file = __MUSIC_PATH__ / 'random_melody.mid'
mid.save(output_file)