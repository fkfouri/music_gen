from scamp import *
from scamp_extensions.parsing.midi import scrape_midi_file_to_dict

from __init__ import JELOUS_GUY_MIDI

midi_data = scrape_midi_file_to_dict(JELOUS_GUY_MIDI)

print(midi_data)


s = Session()
s.tempo = 110

piano = s.new_part("piano")

for wait_time, pitch, length, volume in zip(
    midi_data["inter_onset_times"], midi_data["pitches"], midi_data["lengths"], midi_data["volumes"]
):
    piano.play_note(pitch, volume, length, blocking=False)
    wait(wait_time)
