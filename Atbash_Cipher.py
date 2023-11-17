# https://exercism.org/tracks/python/exercises/atbash-cipher

plain = 'abcdefghijklmnopqrstuvwxyz'
cipher = 'zyxwvutsrqponmlkjihgfedcba'


def encode(plain_text):
    enc = ''
    plain_text = plain_text.replace(" ", "")
    for character in plain_text:
        if character.isalnum():
            if character.isdigit():
                enc += character
            else:
                if character.isupper():
                    index = plain.find(character.lower())
                    enc += cipher[index]
                else:
                    index = plain.find(character)
                    enc += cipher[index]

    return ' '.join(enc[i:i + 5] for i in range(0, len(enc), 5))


def decode(ciphered_text):
    dec = ''
    ciphered_text = ciphered_text.replace(" ", "")
    for character in ciphered_text:
        if character.isdigit():
            dec += character
        else:
            index = plain.find(character)
            dec += cipher[index]
    return dec
