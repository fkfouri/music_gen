from scamp import *

s = Session()

voice = s.new_part("choir aah")
s.start_transcribing()
s.tempo = 120


def is_consonant(p1, p2):
    # unissono (P1), terça menores, terça maiores, Perfect Fourth (P4),
    # Perfect Fifth (P5), sextas menores e sextas maiores
    if abs(p1 - p2) % 12 in [0, 3, 4, 5, 7, 8, 9]:
        return True
    return False


cantus_firmus = [60, 63, 62, 67, 65, 64, 67, 69]
counterpoint = [76]

i = 0

while i < len(cantus_firmus):
    # play the current chord
    voice.play_chord([cantus_firmus[i], counterpoint[i]], 1, 1)

    if i + 1 >= len(cantus_firmus):
        # Last note. No need to figure out the next counterpoint
        break

    # otherwise, figure out the next counterpoint note
    for motion_option in [1, 2, -1, -2, 3, -3, 4, -4]:
        if cantus_firmus[i + 1] > cantus_firmus[i]:
            # Cantus Firmus going up, so prioritize going down
            motion_option *= -1

        if is_consonant(cantus_firmus[i], counterpoint[i] + motion_option):
            counterpoint.append(cantus_firmus[i] + motion_option)

            break
    else:
        # no valid motion option found
        raise RuntimeError("could not find acceptable motion")

    i += 1


print(f"Cantus firmuls: {cantus_firmus}")
print(f"Counterpoint: {counterpoint}")
s.stop_transcribing().to_score().show()
