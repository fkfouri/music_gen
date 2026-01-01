import os
import sys
from datetime import datetime
from pathlib import Path

__THIS_PATH__ = (
    Path(os.path.dirname(sys.executable)) if getattr(sys, "frozen", False) else Path(os.path.dirname(__file__))
)

__ROOT_PATH__ = __THIS_PATH__.parent

__MUSIC_PATH__ = __ROOT_PATH__ / "music"

JELOUS_GUY_MIDI = __MUSIC_PATH__ / "Jealous_guy.mid"