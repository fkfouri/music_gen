# Generate arpeggios

import mido
from __init__ import __MUSIC_PATH__
from mido import Message, MidiFile, MidiTrack

# define our variables
bpm = 120
tickets_per_beat = 480
output_file = __MUSIC_PATH__ / "chord_arpeggios.mid"

chords_progression = [
    [55, 59, 62],  # G major
    [52, 55, 59],  # E minor
    [48, 52, 55],  # C major
    [50, 54, 57],  # D major
]

# Create MIDI file and track
mid = MidiFile()
track = MidiTrack()
mid.tracks.append(track)

# Add tempo message
track.append(mido.MetaMessage("set_tempo", tempo=mido.bpm2tempo(bpm)))


# Add chords to midi
def add_chord(track, chord, ticks_duration):
    for note in chord:
        track.append(Message("note_on", note=note, velocity=64, time=0))

    track.append(Message("note_off", note=note, velocity=64, time=ticks_duration))

    for note in chord[1:]:
        track.append(Message("note_off", note=note, velocity=64, time=0))


# Add arpeggios to the track
def add_arpeggio(track, chord, ticks_per_note):
    # num_notes = len(chord)
    # ticks_per_note = ticks_duration // num_notes

    for note in chord:
        track.append(Message("note_on", note=note, velocity=64, time=0))
        track.append(Message("note_off", note=note, velocity=64, time=ticks_per_note))


# Generate the sequence
for chord in chords_progression:
    # add chord
    add_chord(track, chord, tickets_per_beat)

    # add arpeggio
    add_arpeggio(track, chord, tickets_per_beat // len(chord))


# Save the MIDI file
mid.save(output_file)
