import matplotlib.pyplot as plt
import numpy as np

# create a simple sine wave - 5HZ
t = np.linspace(0, 1, 500)
sine_wave = np.sin(2 * np.pi * 5 * t)

# plot the sine wave
plt.plot(t, sine_wave)
plt.title("5 Hz Sine Wave")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.show()
