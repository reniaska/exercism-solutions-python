# https://exercism.org/tracks/python/exercises/rotational-cipher

def rotate(text, key):
    plain = 'abcdefghijklmnopqrstuvwxyz'
    cipher = plain[key:] + plain[:key]
    coded = ''

    for character in text:
        if not character.isalpha():
            coded += character
        else:
            if character.isupper():
                index = plain.find(character.lower())
                coded += cipher[index].upper()
            else:
                index = plain.find(character)
                coded += cipher[index]
    return coded
