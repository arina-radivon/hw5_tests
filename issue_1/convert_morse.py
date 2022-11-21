LETTER_TO_MORSE = {
    'A': '.-', 'B': '-...', 'C': '-.-.',
    'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..',
    'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-',
    'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '1': '.----',
    '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.', '0': '-----',
    ', ': '--..--', '.': '.-.-.-', '?': '..--..',
    '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-',
    ' ': ' '
}

MORSE_TO_LETTER = {
    morse: letter
    for letter, morse in LETTER_TO_MORSE.items()
}


def encode(message: str) -> str:
    """
    The funtion encode string to morse-string

    1_test:
    >>> encode('SOS')
    '... --- ...'

    2_test:
    It has to work with NORMALIZE_WHITESPACE flag
    >>> encode('WHAT DOES THE FOX SAY?')
    '.-- .... .- -   -.. --- . ...   - .... .
    ..-. --- -..-     ... .- -.-- ..--..'

    3_test:
    Test with exception
    >>> encode('*')
    Traceback (most recent call last):
    KeyError: '*'

    4_test:
    It has to work with ELLIPSIS directive: (ABC...XYZ)
    >>> encode('ABCDEFGHIJKLMNOPQRSTUVWXYZ')  # doctest: +ELLIPSIS
    '.- -... -.-. ... -..- -.-- --..'

    """
    encoded_signs = [
        LETTER_TO_MORSE[letter] for letter in message
    ]

    return ' '.join(encoded_signs)

