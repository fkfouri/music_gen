from scamp import *
from scamp_extensions.pitch import Scale

s = Session()

scale = Scale.octatonic(60)
bassoon = s.new_part("bassoon")

countdown = 0.1
last_position = (0, 0)


def mouse_move_listener(x, y):
    global countdown, last_position

    dx, dy = x - last_position[0], y - last_position[1]

    last_position = (x, y)

    print(last_position, dx, dy)
    countdown -= (dx**2 + dy**2) ** 0.5

    if countdown < 0:
        pitch = scale.round(34 + 40 * (1 - y))
        bassoon.play_note(pitch, x, 0.1, blocking=False)

        countdown = 0.1


s.register_mouse_listener(
    on_move=mouse_move_listener,
    relative_coordinates=True,
)
s.wait_forever()
