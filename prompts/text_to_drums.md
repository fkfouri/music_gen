# Prompt - Text To Drums

I need assistance in producing Al-generated text that I convert to music using drum MIDI files. Initially, I'll provide a description of the format I need for the textual representation of the music. I need to generate rhythm.

Since music is a time-based art form, the notes follow each other in time, and sometimes there are no notes, that is, silences. The way I would like you to generate them is as follows:

Each note is represented with three elements: 

The element of the drumset (integer value) and The duration of the note (float value) and The velocity (so how strong the drum element will sound):

For drum the notes will be:
- 27 High Q (GM2)
- 28 Slap (GM2)
- 29 Scratch Push (GM2)
- 30 Scratch Pull (GM2)
- 31 Sticks (GM2)
- 32 Square Click (GM2)
- 33 Metronome Click (GM2) 
- 34 Metronome Bell (GM2)
- 35 Bass Drum 2
- 36 Bass Drum 1
- 37 Side Stick
- 38 Snare Drum 1
- 39 Hand Clap
- 40 Snare Drum 2
- 41 Low Tom 2
- 42 Closed Hi-hat
- 43 Low Tom 1
- 44 Pedal Hi-hat
- 45 Mid Tom 2
- 46 Open Hi-hat
- 47 Mid Tom 1
- 48 High Tom 2
- 49 Crash Cymbal 1
- 50 High Tom 1
- 51 Ride Cymbal 1
- 52 Chinese Cymbal
- 53 Ride Bell
- 54 Tambourine
- 55 Splash Cymbal
- 56 Cowbell
- 57 Crash Cymbal 2 58 Vibra Slap
- 59 Ride Cymbal 2
- 60 High Bongo
- 61 Low Bongo
- 62 Mute High Conga
- 63 Open High Conga
- 64 Low Conga
- 65 High Timbale
- 66 Low Timbale
- 67 High Agogo
- 68 Low Agogo
- 69 Cabasa
- 70 Maracas
- 71 Short Whistle
- 72 Long Whistle
- 73 Short Guiro
- 74 Long Guiro
- 75 Claves
- 76 High Wood Block
- 77 Low Wood Block
- 78 Mute Cuica
- 79 Open Cuica
- 80 Mute Triangle
- 81 Open Triangle
- 82 Shaker
- 83 Jingle Bell
- 84 Belltree
- 85 Castanets
- 86 Mute Surdo
- 87 Open Surdo
- 88 High Q (GM2)
- 89 Slap (GM2)
- 90 Scratch Push (GM2)
- 91 Scratch Pull (GM2)
- 92 Sticks (GM2)
- 93 Square Click (GM2)
- 94 Metronome Click (GM2)
- 95 Metronome Bell (GM2)
- 96 Bass Drum 2
- 97 Bass Drum 1    
- 98 Side Stick
- 99 Snare Drum 1
- 100 Hand Clap
- 101 Snare Drum 2
- 102 Low Tom 2
- 103 Closed Hi-hat
- 104 Low Tom 1
- 105 Pedal Hi-hat
- 106 Mid Tom 2
- 107 Open Hi-hat
- 108 Mid Tom 1
- 109 High Tom 2
- 110 Crash Cymbal 1
- 111 High Tom 1
- 112 Ride Cymbal 1
- 113 Chinese Cymbal
- 114 Ride Bell
- 115 Tambourine
- 116 Splash Cymbal
- 117 Cowbell
- 118 Crash Cymbal 2
- 119 Vibra Slap
- 120 Ride Cymbal 2
- 121 High Bongo
- 122 Low Bongo
- 123 Mute High Conga
- 124 Open High Conga
- 125 Low Conga
- 126 High Timbale
- 127 Low Timbale
- 128 High Agogo

The duration of the note (float value) represented as:
- 0.125 for an eighth note
- 0.25 for a quarter note
- 0.5 for a half note
- 1 for a whole note
- 2 for a double whole note

But it could be any number between 0 and 2, because you know, musicians are creative so why not 0.29 or 1.22, etc.

And when there is a silence the note should be 0 and the duration is how long is that silence.
 
Feel free to use intricate durations and notes.

And the velocity is from 0 to 127

SO what i need is:

```
drum_pitch_duration_data = [
((note, note), duration, velocity), (note, duration, velocity), (note,note, note), duration, velocity),...,
]
etc,
```

So, in the same moment it could be one or more than one element in the drum pattern or a silence or just one element, or two, or more.

The time signature of a piece of music tells you how many beats are in each measure and what kind of note gets one beat. The most common time signatures are 4/4 and 3/4.

In 4/4 time, there are four beats in each measure and each beat is a quarter note. This means that a measure of 4/4 is four quarter notes long.

In 3/4 time, there are three beats in each measure and each beat is a quarter note. This means that a measure of 3/4 is three quarter notes long.

The difference between 4/4 and 3/4 is the number of beats in each measure. 4/4 has four beats per measure, while 3/4 has three beats per measure. This difference in the number of beats can affect the feel of the music. 4/4 is often used in music that is upbeat and energetic, while 3/4 is often used in music that is slower and more relaxed.

The time signature of a piece of music can also affect the way that the drums are played. In 4/4 time, the drums are often played on the beats 1, 
2, 3, and 4. In 3/4 time, the drums are often played on the beats 1, 2, and 3.

There are many other time signatures besides 4/4 and 3/4. Here are a few examples: 2/4 (fast upbeat), 6/8 (folk-inspired), 9/8 (Middle Eastern or Indian inspired), 12/8 (jazz-inspired)

Now that you have a full understanding of the text representation, we will create some awesome drum patterns!
Are you ready to start generating drums sequences?

If so, respond with 'YES' and nothing else. Do not give me anything until I ask for some kind of
music, just answer "YES" if you have the
concept.