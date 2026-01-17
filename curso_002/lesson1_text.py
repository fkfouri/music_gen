# from scamp import *
import scamp as sc

s = sc.Session()
piano = s.new_part("Piano")

text = "Dante Kfouri"
text += " 2024!"

for char in text:
    if char == " ":
        sc.wait(0.2)
    elif char.isalnum():
        piano.play_note(ord(char) - 20, 0.5, 0.06)
    else:
        sc.wait(0.2)
        piano.play_note(ord(char), 0.8, 0.06)
        sc.wait(0.2)
