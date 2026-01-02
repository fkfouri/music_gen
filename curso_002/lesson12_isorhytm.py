from scamp import *
from itertools import cycle

# for x in cycle( [2,7,4]):
#     print(x)
#     wait(.5)


# for x,y in zip(cycle( [2,7,4]), cycle([30,20,10,100,200])):
#     print(x,y)
#     wait(.5)


s = Session(tempo=90)

#

# for pitch, dur in zip(cycle([69, 72, 71, 64, 66, None, 62]), cycle([1,.5,.75,.25,1])):
#     volume = .7
#     oboe.play_note(pitch, volume, dur)


def do_isorhytm(inst, color, talea, voluminor=(1.0,)):
    for pitch, volume, dur in zip(cycle(color), cycle(voluminor), cycle(talea)):
        inst.play_note(pitch, volume, dur)


oboe = s.new_part("oboe")
clarinet = s.new_part("clarinet")

fork(
    do_isorhytm,
    args=(
        oboe,
        [69, 72, 71, 64, 66, None, 62],
        [1, 0.5, 0.75, 0.25, 1],
        [0.5, 0.7, 0.3],
    ),
)
fork(
    do_isorhytm,
    args=(
        clarinet,
        [76, 78, 77, 79, None],
        [2, 0.5, 1],
        [0.3, 0.5, 0.4, 0.6, 0.9, 0.6, 0.4],
    ),
)

wait_forever()
