import  numpy as np
import simpleaudio as sa

# *************************** Play sounds using NumPy and Simpleaudio *****************************
frequency = 600
duration = 396
sample_rate = 44100
amplitude = 0.5

# Generate time values for the waveform
duration_seconds = duration / 1000
t = np.linspace(0, duration_seconds, int(sample_rate * duration_seconds), False)

# Generate sine wave for the tone
tone = np.sin(2 * np.pi * frequency * t)

# Adjust Amplitude
tone *= amplitude

# Convert to 16-bit PCM format
audio = (tone * 32767).astype(np.int16)

#Play the sound using simpleaudio
play_obj = sa.play_buffer(audio, 1, 2, sample_rate)
play_obj.wait_done()