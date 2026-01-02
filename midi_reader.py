from mido import MidiFile

mid = MidiFile("Jealous_guy.mid", clip=True)

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


for msg in mid:
    current_time += msg.time

    if msg.type == "note_on" and msg.velocity > 0:
        active_notes[(msg.channel, msg.note)] = current_time

    elif msg.type in ("note_off", "note_on") and msg.velocity == 0:
        key = (msg.channel, msg.note)
        if key in active_notes:
            start = active_notes.pop(key)
            duration = current_time - start

            note_data = {"note": msg.note, "start": start, "duration": duration}

            # 🎯 DRUMS (canal 10 → index 9)
            if msg.channel == 9:
                drums.append(note_data)

            # 🎵 Melodia (heurística simples)
            elif msg.channel in [0, 1]:
                melody.append(note_data)

            # 🎹 Acordes
            else:
                chords.append(note_data)

x = 1
