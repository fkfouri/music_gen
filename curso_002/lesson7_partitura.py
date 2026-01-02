from scamp import *

# import abjad
# string = "c'16 f' g' a' d' g' a' b' e' a' b' c'' f' b' c'' d''16"
# voice_1 = abjad.Voice(string, name="Voice_1")
# staff_1 = abjad.Staff([voice_1], name="Staff_1")
# abjad.show(staff_1)

s = Session()

piano1 = s.new_part("piano")
piano2 = s.new_part("piano")

pitches = [64, 66, 71, 73, 74, 66, 64, 73, 71, 66, 74, 73]


def piano_part(which_piano):
    while True:
        for pitch in pitches:
            which_piano.play_note(pitch, 1, 0.25)
    # piano2.play_note(pitch + 12, 0.7, 0.4)


# piano_part(piano1)


clock1 = s.fork(piano_part, args=(piano1,), initial_tempo=100)
clock2 = s.fork(piano_part, args=(piano2,), initial_tempo=99)

# wait_forever()

s.start_transcribing(clock=clock1)
s.wait(10)

performance = s.stop_transcribing()
performance.to_score(
    QuantizationScheme.from_time_signature("3/4", 16),
    title="Teste Kfouri",
    composer="Last Nobler",
).show()
