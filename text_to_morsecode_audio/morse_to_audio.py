import argparse
from pathlib import Path
import numpy as np
import simpleaudio as sa
import math

# Morse code timing
DOT_DURATION = 0.1
DASH_DURATION = DOT_DURATION * 3
INTRA_CHAR_GAP = DOT_DURATION  # Gap between dots/dashes in a character
INTER_CHAR_GAP = DOT_DURATION * 3  # Gap between characters
WORD_GAP = DOT_DURATION * 7  # Gap between words

# Default audio parameters
FREQUENCY = 600
SAMPLE_RATE = 44100
VOLUME = 0.3

# Morse code symbols
DOT = '.'
DASH = '-'
SYMBOL_GAP = ' '
WORD_SEPARATOR = '/'

MORSE_CODE_DICT = {
    'A': '.-',    'B': '-...',  'C': '-.-.',  'D': '-..',
    'E': '.',     'F': '..-.',  'G': '--.',   'H': '....',
    'I': '..',    'J': '.---',  'K': '-.-',   'L': '.-..',
    'M': '--',    'N': '-.',    'O': '---',   'P': '.--.',
    'Q': '--.-',  'R': '.-.',   'S': '...',   'T': '-',
    'U': '..-',   'V': '...-',  'W': '.--',   'X': '-..-',
    'Y': '-.--',  'Z': '--..',

    '0': '-----', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.',

    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.',
    '!': '-.-.--', '/': '-..-.',  '(': '-.--.',  ')': '-.--.-',
    '&': '.-...',  ':': '---...', ';': '-.-.-.', '=': '-...-',
    '+': '.-.-.',  '-': '-....-', '_': '..--.-', '"': '.-..-.',
    '$': '...-..-', '@': '.--.-.',

    ' ': '/'
}

def text_to_morse():
    user_input = input('What would you like to translate to Morse Code?\n').upper()
    # Error handling to show unconvertible characters

    invalid_chars = [char for char in user_input if char not in MORSE_CODE_DICT]

    if invalid_chars:
        print(f"Sorry, the following character(s) cannot be converted to Morse Code: {', '.join(invalid_chars)}")
        print("Try a different input.")
        return text_to_morse()
    else:

        return ' '.join(MORSE_CODE_DICT[letter] for letter in user_input)


def translate_more_text():
    while True:
        more_words = input('Would you like to translate more words (Y/n)? \n').upper()
        if more_words == 'Y':
            morse = text_to_morse()
            print('Morse:', morse)
            waveform = morse_to_waveform(morse)
            play_waveform(waveform)
        elif more_words == 'N':
            print('END!')
            break
        else:
            print('Not a valid choice try again!')


def morse_to_waveform(morse_code, frequency=FREQUENCY, dot_duration=DOT_DURATION, sample_rate=SAMPLE_RATE, volume=VOLUME):
    """
    Convert a Morse code string to a numpy waveform.
    """
    # Tones and Silences
    def tone(duration):
        t = np.linspace(0, duration, int(sample_rate * duration), False)
        return np.sin(2 * np.pi * frequency * t) * volume
    dot_tone = tone(dot_duration)
    dash_tone = tone(DASH_DURATION)
    intra_char_silence = np.zeros(int(sample_rate * INTRA_CHAR_GAP))
    inter_char_silence = np.zeros(int(sample_rate * (INTER_CHAR_GAP - INTRA_CHAR_GAP)))
    word_silence = np.zeros(int(sample_rate * (WORD_GAP - INTER_CHAR_GAP)))

    waveform = []
    words = morse_code.strip().split(WORD_SEPARATOR)
    for w_idx, word in enumerate(words):
        chars = word.strip().split(SYMBOL_GAP)
        for c_idx, char in enumerate(chars):
            for s_idx, symbol in enumerate(char):
                if symbol == DOT:
                    waveform.append(dot_tone)
                elif symbol == DASH:
                    waveform.append(dash_tone)
                # Add intra-character gap if not last symbol
                if s_idx < len(char) - 1:
                    waveform.append(intra_char_silence)
            # Add inter-character gap if not last char
            if c_idx < len(chars) - 1:
                waveform.append(inter_char_silence)
        # Add word gap if not last word
        if w_idx < len(words) - 1:
            waveform.append(word_silence)
    if waveform:
        return np.concatenate(waveform)
    else:
        return np.array([], dtype=np.float32)


def play_waveform(waveform, sample_rate=SAMPLE_RATE):
    if waveform is None or len(waveform) == 0:
        print("No audio to play.")
        return
    if np.any(np.isnan(waveform)) or np.any(np.isinf(waveform)):
        print("Waveform contains NaN or Inf values. Skipping playback.")
        return
    if waveform.ndim != 1:
        print(f"Waveform is not 1D (shape: {waveform.shape}). Skipping playback.")
        return
    print(f"Playing waveform: dtype={waveform.dtype}, shape={waveform.shape}, min={np.min(waveform)}, max={np.max(waveform)}")
    try:
        audio = (waveform * 32767).astype(np.int16)
        sa.play_buffer(audio, 1, 2, sample_rate).wait_done()
    except Exception as e:
        print(f"Error playing audio: {e}")


def save_waveform(waveform, path, sample_rate=SAMPLE_RATE):
    import wave
    audio = (waveform * 32767).astype(np.int16)
    with wave.open(str(path), 'wb') as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(sample_rate)
        wf.writeframes(audio.tobytes())


def main():
    parser = argparse.ArgumentParser(description="Convert Morse code to audio.")
    parser.add_argument('-i', '--input', type=str, required=True,
                        help="Morse code input string or path to a file containing Morse code.")
    parser.add_argument('-f', '--frequency', type=int, default=FREQUENCY, help="Tone frequency in Hz (default: 600)")
    parser.add_argument('-d', '--dot', type=float, default=DOT_DURATION, help="Dot duration in seconds (default: 0.1)")
    parser.add_argument('-o', '--output', type=str, help="Path to save the output .wav file (optional)")
    parser.add_argument('--play', action='store_true', help="Play the audio after generating.")
    args = parser.parse_args()

    # Determine if input is a file or direct Morse code string
    input_path = Path(args.input)
    if input_path.exists():
        morse_code = input_path.read_text().strip()
    else:
        morse_code = args.input.strip()

    waveform = morse_to_waveform(
        morse_code,
        frequency=args.frequency,
        dot_duration=args.dot,
        sample_rate=SAMPLE_RATE,
        volume=VOLUME
    )

    if args.output:
        save_waveform(waveform, Path(args.output), sample_rate=SAMPLE_RATE)
        print(f"Audio saved to {args.output}")
    if args.play or not args.output:
        play_waveform(waveform, sample_rate=SAMPLE_RATE)


if __name__ == "__main__":
    # Comment out main() to disable the Command-Line Mode and run the code in Interactive Mode
    # to ensure the translate_more_text() gets called after the other functions
    # main()


    try:
        morse = text_to_morse()
        print('Morse:', morse)
        waveform = morse_to_waveform(morse)
        play_waveform(waveform)
        translate_more_text()
    except (SystemExit, KeyboardInterrupt):
        print("Exiting...")
    except Exception as e:
        print(f"Unexpected error: {e}")
        import traceback
        traceback.print_exc()
        print("If you see 'Process finished with exit code 139', this is likely a native library crash (e.g., simpleaudio or numpy). Check your input and environment.")
