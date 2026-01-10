import os
import sys
from pathlib import Path

import pytest
import scamp

__THIS_PATH__ = (
    Path(os.path.dirname(sys.executable)) if getattr(sys, "frozen", False) else Path(os.path.dirname(__file__))
)

__ROOT_PATH__ = __THIS_PATH__.parent

__MUSIC_PATH__ = __ROOT_PATH__ / "music"

JELOUS_GUY_MIDI = __MUSIC_PATH__ / "Jealous_guy.mid"


@pytest.fixture()
def SESSION():
    s = scamp.Session()
    s.tempo = 80
    yield s
    s.kill()


@pytest.fixture()
def PIANO(SESSION):
    piano = SESSION.new_part("Piano")
    yield piano

@pytest.fixture()
def GUITAR(SESSION):
    guitar = SESSION.new_part("Acoustic Guitar (nylon)")
    yield guitar

@pytest.fixture()
def CHURCH_ORGAN(SESSION):
    organ = SESSION.new_part("church organ")
    yield organ


@pytest.fixture()
def MIDI_FILE():
    return JELOUS_GUY_MIDI
    return __MUSIC_PATH__ / "c_chord.mid"
