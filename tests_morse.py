import doctest
from morse import LETTER_TO_MORSE


def encode(message: str) -> str:
    """
    Кодирует строку в соответсвие с таблицей азбуки Морзе

    >>> encode('SOS')
    '... --- ...'
    >>> encode("AAA BBB AAA") # doctest: +ELLIPSIS
    '.- .- .- ... .- .- .-'
    >>> encode("AAA BBB                AAA") # doctest: +NORMALIZE_WHITESPACE
    '.- .- .-   -... -... -...   .- .- .-'
    >>> encode('abc')
    Traceback (most recent call last):
    KeyError: 'a'
    """
    encoded_signs = [
        LETTER_TO_MORSE[letter] for letter in message
    ]

    return ' '.join(encoded_signs)


if __name__ == '__main__':
    doctest.testmod()
