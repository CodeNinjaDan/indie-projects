import  numpy as np
import simpleaudio as sa
import time

# *************************** Play sounds using NumPy and Simpleaudio *****************************
# frequency = 600
# duration = 396
# sample_rate = 44100
# amplitude = 0.5
#
# # Generate time values for the waveform
# duration_seconds = duration / 1000
# t = np.linspace(0, duration_seconds, int(sample_rate * duration_seconds), False)
#
# # Generate sine wave for the tone
# tone = np.sin(2 * np.pi * frequency * t)
#
# # Adjust Amplitude
# tone *= amplitude
#
# # Convert to 16-bit PCM format
# audio = (tone * 32767).astype(np.int16)
#
# #Play the sound using simpleaudio
# play_obj = sa.play_buffer(audio, 1, 2, sample_rate)
# play_obj.wait_done()


# ********************************* Add a silences between tones using time.sleep ***********************************

# sample_rate = 44100
# volume = 0.3
#
# def play_tone(frequency, duration_sec):
#     t = np.linspace(0, duration_sec, int(sample_rate * duration_sec), False)
#     tone = np.sin(2 * np.pi * frequency * t) * volume
#     audio = (tone * 32767).astype(np.int16)
#     sa.play_buffer(audio, 1, 2, sample_rate).wait_done()
#
# # Play a dot
# play_tone(600, 0.1)  # 100ms
# time.sleep(0.1)      # Silence between dot and next tone
#
# # Play a dash
# play_tone(600, 0.3)


# ************************ Add silences between tones using np.zero ******************************

sample_rate = 44100
volume = 0.3

# Dot tone: 600Hz for 132ms
t_dot = np.linspace(0, 0.132, int(sample_rate * 0.1), False)
dot = np.sin(2 * np.pi * 600 * t_dot) * volume

# Dash tone: 600Hz for 396ms
t_dash = np.linspace(0, 0.396, int(sample_rate * 0.3), False)
dash = np.sin(2 * np.pi * 600 * t_dash) * volume

# Silence of 100ms
silence = np.zeros(int(sample_rate * 0.1))

# Combine: dot + silence + dash
waveform = np.concatenate((dot, silence, dash))

# Convert to 16-bit PCM and play
audio = (waveform * 32767).astype(np.int16)
sa.play_buffer(audio, 1, 2, sample_rate).wait_done()
