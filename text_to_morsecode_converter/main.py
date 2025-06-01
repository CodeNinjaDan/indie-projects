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

def translate():
    user_input = input('What would you like to translate to Morse Code?\n').upper()

        # Error handling to show unconvertible characters

        # invalid_chars = [char for char in user_input if char not in MORSE_CODE_DICT]
        #
        # if invalid_chars:
        #     print(f"Sorry, the following character(s) cannot be converted to Morse Code: {', '.join(invalid_chars)}")
        #     print("Try a different input.")
        #     translate()
        # else:
        #     morse_translation = ' '.join(MORSE_CODE_DICT[letter] for letter in user_input)
        #     print(morse_translation)
        #     translate_more()
    try:
        morse_translation = ' '.join(MORSE_CODE_DICT[letter] for letter in user_input)
        print(morse_translation)

        translate_more()

    except KeyError:
        print('Character(s) entered cannot be translated to Morse Code :( \nTry a different character(s)')
        translate()


def translate_more():
    more_words = input('Would you like to translate more words (Y/n)? \n').upper()
    if more_words == 'Y':
        translate()

    elif more_words == 'N':
        print('END!')

    else:
        print('Not a valid choice try again!')
        translate_more()


translate()
