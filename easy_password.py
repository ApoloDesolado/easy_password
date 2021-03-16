import secrets
import re

"""
This script helps you to generate rememorable strong
        passwords given a phrase you like.

The function "passwords" requires 3 arguments:
    phrase:       the phrase you like (must have an acceptable lenght)
    password_len: lenght of the desired password (recommended to be higher than 10)
    alternatives: number of generated passwords to return (mainly to chose the one you like the most)

this function will return:
    Bool, str
    The boolean value is wether or not it's possible to generate the password.
    The string is the reason of why it isn't possible (too short or too long)
"""

# This contstant defines how many characters will be reservated from each trimmed word.
RESERVATED=1

# These are the possible replacements for each character, it contains symbols, numbers and uppercased characters.
replacements={
        "a":["a", "@", "4"], "b":["b", "6"], "c":["c", "("], "d":["d", "D"],
        "e":["e", "3"], "f":["f", "F"], "g":["g", "G", "9", "&"], "h":["h", "H"],
        "i":["i", "I", "¡", "1"], "j":["j", "J"], "k":["k", "K"], "l":["l", "L" "1", "["],
        "m":["m", "M"], "n":["n", "N"], "ñ":["ñ", "Ñ"], "o":["o", "O", "0"], "p":["p", "P", "?"],
        "q":["q", "9", "Q"], "r":["r", "R"], "s":["s", "S", "$", "5"], "t":["t", "T", "7"], "u":["u", "U"],
        "v":["v", "V"], "w":["w", "W"], "x":["x", "X", "?"], "y":["y","Y", "&"], "z":["z", "Z", "2"]
}

def replace_chars(word):

    # Randomly chooses characters from each trimmed word, then it randomly chooses a replacement from.
    # the replacements dictionary.
    replaced=''.join(x for x in ([secrets.choice(replacements[char]) for char in word if char in replacements]))
    return replaced

def list_len(elements): return sum(len(element) for element in elements)

def shorten_words(words, password_len):
    words_len=list_len(words)
    # Trim the words but only to be equal or longer than
    # the required lenght.
    while words_len != password_len:
        # Randomly picked word to be trimmed.
        chosen = secrets.choice(words)
        if len(chosen) > 1:
            to_remove=list(chosen[1:])
            # Choose random character to remove.
            to_remove.remove(secrets.choice(to_remove))
            trimmed = (f"{chosen[0]}{''.join(i for i in to_remove)}")
            # Replace the original word with the trimmed one.
            words[words.index(chosen)] = trimmed
            words_len = list_len(words)
    return words

def password(phrase, password_len):
    phrase=phrase.lower()
    # Get alphanumeric charachters from the phrase.
    alpha_n_words=re.finditer("\w+", phrase)
    words=[ phrase[m.start():m.end()] for m in alpha_n_words ]
    # Get randomly trimmed versions of the words.
    words = shorten_words(words, password_len)
    # Randomly replaces characters choosen from replacements dictionary.
    words=[replace_chars(word) for word in words]
    password = ''.join(word for word in words)
    return password

def is_possible(phrase, password_len):
    # Checks if it's possible to generate a password considering:
        # lenght of the phrase, password lenght, and the RESERVATED constant.
    alpha_n_words=re.finditer("\w+", phrase)
    words=[ phrase[m.start():m.end()] for m in alpha_n_words ]
    if list_len(words) < password_len + password_len/RESERVATED:
        restant= int((password_len + password_len/RESERVATED)-list_len(words))
        return False, f"Too short, add {restant} characters."
    elif len(words) > password_len:
        excedent=len(words)-password_len
        return False, f"Too long, remove {excedent} words."
    else:
        return True, ""

def passwords(phrase: str, password_len: int, alternatives: int) -> list :
    # Genertes 5 passwords from the given arguments.
    return [password(phrase, password_len) for _ in range(alternatives)]
