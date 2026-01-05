# https://youtu.be/RddfomrECPA?list=PL_yUKG0GRuliL65l_qEG1uwCC03X4jioL

from scamp import *
import random

s = Session(tempo=100)

# drums = s.new_midi_part("drums", "IAC Bus 1", start_channel=0, num_channels=1)
bass = s.new_midi_part("slap bass", "IAC Bus 1", start_channel=2, num_channels=1)
# bass.send_midi_cc(14, 0)
# exit()

theramin = s.new_midi_part("theramin", "IAC Bus 1", start_channel=1, num_channels=1)

# usado para enviar CCs diretamente e configurar um parametro do canal midi

# https://scamp.marcevanstein.com/scamp/scamp.instruments.ScampInstrument.html#scamp.instruments.ScampInstrument.send_midi_cc
theramin.send_midi_cc(15, 0) # primeiro parametro vai de 0 a 127 e o segundo de 0 a 1
exit()


# drums = s.new_part("drums")
# theramin = s.new_part("theramin")
# bass = s.new_part("slap bass")

pitches = [69,70,67,66]
durs = [1,2,2,3]

while True:
    random.shuffle(pitches)
    random.shuffle(durs)
    for p,d in zip(pitches,durs):
        theramin.play_note(p, .8, d * .5, {"param_15" : random.random()})
    wait(5)
    # drums.play_note(38, 1, 1) 
    # # drums.play_note(38, 1, random.uniform(0.2, 1.3))  # random.randint(38, 1, 1)
    # # theramin.play_note([80, 78], 1, random.uniform(0.2, 1.3))
    # theramin.play_note(80, 1, .2 )
    # bass.play_note(random.randint(36, 45), 1, random.uniform(0.2, 1.3))
