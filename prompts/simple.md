
hey, give me a text representation of a MIDI file but in a simplified version: 

Each note is represented as a tuple of two elements:
- The pitch of the note (integer value).
- The duration of the note (float value) represented as:
    - 0.125 for an eighth note
0   - .25 for a quarter note
    - 0.5 for a half note
    - 1 for a whole note
    - 2 for a double whole note

To represent multiple tracks, use a list of tuples where each tuple contains the notes of the track and its duration.

With this format give me a text representation for a MIDI in the style of Aphex Twin, with multiple tracks, melody, bass, chords, drums...