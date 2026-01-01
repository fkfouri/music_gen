import pygame
from __init__ import JELOUS_GUY_MIDI, __MUSIC_PATH__

MUSIC = __MUSIC_PATH__ / 'random_melody.mid'
MUSIC = JELOUS_GUY_MIDI
MUSIC = __MUSIC_PATH__ / 'c_chord.mid'
MUSIC = __MUSIC_PATH__ / 'chord_arpeggios.mid'
MUSIC = __MUSIC_PATH__ / 'rock_drums.mid'

# pygame initialization
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(MUSIC)
pygame.mixer.music.play()

#keep the program running until the music finishes
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)