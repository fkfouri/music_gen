# DRUMs

import mido
from __init__ import __MUSIC_PATH__
from mido import Message, MetaMessage, MidiFile, MidiTrack

drums = {
    "bass_drum": 36,  # Bass Drum
    "snare": 38,  # Snare Drum
    "closed_hat": 42,  # Closed Hi-Hat
    "open_hat": 46,  # Open Hi-Hat
    "crash": 49,  # Crash Cymbal
}


# Part 2: Generate a simple drum pattern (e.g., basic rock beat)
def generate_drum_pattern(length):  # _in_bars=4, beats_per_bar=4):
    drum_pattern = []
    for i in range(length):
        # Basic rock beat pattern
        if i % 4 == 0:
            drum_pattern.append((drums["bass_drum"], 64))  # Bass drum on beat 1
        elif i % 4 == 2:
            drum_pattern.append((drums["snare"], 40))  # Snare on beat 3
        elif i % 2 == 1:
            drum_pattern.append((drums["closed_hat"], 64))  # Hi-hat on every beat
        elif i % 4 == 3:
            drum_pattern.append((drums["crash"], 50))  # Open hi-hat on the "and" of beat 4
        else:
            drum_pattern.append((None, 0))  # No drum hit
    return drum_pattern


# part 3: Create MIDI file and track
bpm = 120
ticks_per_beat = 480
output_file = __MUSIC_PATH__ / "rock_drums.mid"

mid = MidiFile()
track = MidiTrack()
mid.tracks.append(track)

# Add tempo message
tempo = mido.bpm2tempo(bpm)  # convert bpm to microseconds per beat
track.append(MetaMessage("set_tempo", tempo=tempo))

# Part 4: Generate drum pattern for 4 bars
drum_pattern = generate_drum_pattern(length=240)  # create 240 steps - 1 minute at 120 bpm

# Part 5: Add continuous drum pattern to midi track
for i in range(len(drum_pattern)):
    note, velocity = drum_pattern[i]
    if note is not None:
        track.append(Message("note_on", channel=9, note=note, velocity=velocity, time=0))
        track.append(Message("note_off", channel=9, note=note, velocity=velocity, time=ticks_per_beat))
    else:
        # If no drum hit, just advance the time
        track.append(Message("note_off", channel=9, note=0, velocity=0, time=ticks_per_beat))


# Save the MIDI file
mid.save(output_file)
