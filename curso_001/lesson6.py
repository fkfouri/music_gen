# Draw a spectrogram of an audio file

import librosa
import librosa.display
import matplotlib.pyplot as plt
from __init__ import __MUSIC_PATH__

music_file = __MUSIC_PATH__ / "c_chord.wav"


# Load the audio file
audio, sr = librosa.load(music_file)


# plot the Waveform
plt.figure(figsize=(10, 6))
librosa.display.waveshow(audio, sr=sr)
plt.title("Waveform of c_chord.wav")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.show()


# plot the Spectrogram
X = librosa.stft(audio)
Xdb = librosa.amplitude_to_db(abs(X))
plt.figure(figsize=(10, 6))
librosa.display.specshow(Xdb, sr=sr, x_axis="time", y_axis="hz")
plt.colorbar(format="%+2.0f dB")
plt.title("Spectrogram of c_chord.wav")
plt.show()

# plot the Mel Spectrogram
plt.figure(figsize=(10, 6))
librosa.display.specshow(librosa.feature.melspectrogram(y=audio, sr=sr), sr=sr, x_axis="time", y_axis="mel")
plt.colorbar(format="%+2.0f dB")
plt.title("Mel Spectrogram of c_chord.wav")
plt.show()
