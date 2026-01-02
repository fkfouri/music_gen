from __init__ import JELOUS_GUY_MIDI
from mido import MidiFile

mid = MidiFile(JELOUS_GUY_MIDI)

chords = []
melody = []
drums = []

active_notes = {}  # {(channel, note): start_time}
current_time = 0
x = []

# port = mido.open_output()
# # outport.send(msg)

# for msg in mid.play():
#     x = msg
#     port.send(msg)

for i, track in enumerate(mid.tracks):
    print(f"Track {i}: {track.name}")
    for msg in track:
        print(msg)
