from scamp import *

s = Session()
s.tempo = 120
instr = s.new_part("piano")


def keyboard_listener(key, code):
    """
    Docstring for keyboard_listener

    :param key: Description
    :param code: Description

    Depende de pynput
    """

    if len(key) == 1:
        if key.isalnum():
            pitch = ord(key) - 20
            volume = 0.5
            length = 0.06
            blocking = False
        else:
            pitch = ord(key)
            volume = 1.0
            length = 0.06

        # print(f"Played note: {key} ({pitch})")
        instr.play_note(pitch, volume, length, blocking=blocking)
        print(f"{key}:{code}", end=" ")


s.register_keyboard_listener(keyboard_listener)
s.wait_forever()
