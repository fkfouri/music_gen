import mido
import pygame
from __init__ import __MUSIC_PATH__

music = __MUSIC_PATH__ / 'c_chord.mid'

mid = mido.MidiFile()
track = mido.MidiTrack()
mid.tracks.append(track)

# Mido note number for the C chord stored in a list with duration

c_chord_notes = [(60, 480), (64, 480), (67, 480)]  # C4, E4, G4 with duration 480 ticks

for note, duration in c_chord_notes:
    track.append(mido.Message('note_on', note=note, velocity=64, time=0))
    track.append(mido.Message('note_off', note=note, velocity=64, time=duration))



mid.save(music)


# pygame initialization
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(music)
pygame.mixer.music.play()

#keep the program running until the music finishes
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)
