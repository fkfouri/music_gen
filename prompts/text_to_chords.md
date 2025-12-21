# Prompt - Text To Chords

I need assistance in producing AI-generated text that I convert to music using MIDI files. Initially,I'll provide a description of the format I need for the textual representation of the music.Since music is a time-based art form,the notes follow each other in time, andsometimes there are no notes, that is, silences.Here I need you to generate Chords, so, more than one note each time, could be 2, 3, 4, etc.

The way I would like you to generate them is as follows:

Each chord is represented these elements:

The pitches of the notes (integer values).

Because I will use this text representation and convert to MIDI the note should be a number from 21 (that is note A0 - 27.50Hz) to 96 (that os C7 - 2093 hz) so use these number to represent the note.

The duration of the note (float value) represented as:
- 0.125 for eight note
- 0.25 fora a quarter note
- 0.5 fora a half note
- 1 for a whole note
- 2 for a double whole note

But it could be any number between 0 and 2, because you know, musicians are creative so why not 0.29 or 1.22, etc.

Whit this format i need you generate a text that I will cover in music in this format:

```
chords_pith_duration_data = [
	((note, note, note), duration), ((note,note), duration), (note, duration), etc
]

And when there is a silence the note should be 0 and the duration is how long is that silence
```

The key is Harmony is that is the vertical aspect of music, or the combination of different pitches sounding at the same time. Chords are the building blocks of harmony, and they are made up of two or more notes that are played together.

The simplest type of chord is a two-note chord, also known as a diatonic chord. Diatonic chords are made up of two notes that are next to each other on the musical scale. For example, a C major chord is made up of the notes C and E.

Three-note chords are also known as triads. Triads are made up of a root note, a third, and a fifth. The root note is the lowest note in the chord, the third is the note that is two semitones above the root, and the fifth is the note that is seven semitones above the root. For example, a C major triad is made up of the notes C, E, and G.

Four-note chords are also known as seventh chords. Seventh chords are made up of a root note, a third, a fifth, and a seventh. The seventh note can be either major or minor. For example, a C major seventh chord is made up of the notes C, E, G, and B.

And you also have:

- Sus chords: Sus chords are made up of a root note, a third, and a fifth, but the third is replaced with a suspended fourth or second. For example, a Csus4 chord is made up of the notes C, F, and G.
- Add chords: Add chords are made up of a root note, a third, a fifth, and an additional note. For example, a Cadd9 chord is made up of the notes C, E, G, and B.


- Augmented chords: Augmented chords are made up of a root note, a major third, and a perfect fifth. For example, a C augmented chord is made up of the notes C, E#, and G#.
- Diminished chords: Diminished chords are made up of a root note, a minor third, and a diminished fifth. For example, a C diminished chord is made up of the notes C, Eb, and Gb.
- Harmony is an important part of music, and it can be used to create a variety of different moods and emotions. For example, major chords are often used to create a sense of happiness or joy, while minor chords are often used to create a sense of sadness or melancholy.

Please note that Al-generated music may not sound pleasing as it is randomly generated so we will use music theory but not random math so don't randomize the generation process. take into account musical concepts like scales, modes, etc.

Now that you have a full understanding of the representation, we will create some awesome music!

Are you ready to start generating music?
If so, respond with "YES" and nothing else.
