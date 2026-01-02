from scamp import settings, test_run

settings.audio_driver = "sounddevice"
settings.audio_driver = "pygame"
test_run.play(show_lilypond=True)
