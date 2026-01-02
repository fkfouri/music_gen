# https://en.wikipedia.org/wiki/Pisano_period
from scamp import *

s = Session(tempo=120)

clarinet = s.new_part("clarinet")

a = b = 1
while True:
    print(a, end=", ")
    # wait(.2)
    clarinet.play_note(64 + a, 0.7, 0.25)
    # a, b = b, a + b #=> Problema que o fibonnacci cresce muito rápido
    a, b = b, (a + b) % 12  # Corrige o problema do fibonnacci
c
