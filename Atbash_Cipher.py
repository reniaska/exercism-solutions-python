#https://exercism.org/tracks/python/exercises/atbash-cipher

plain = 'abcdefghijklmnopqrstuvwxyz'
cipher = 'zyxwvutsrqponmlkjihgfedcba'


def encode(plain_text):
    encode = ''
    idx = 0
    plain_text = plain_text.replace(" ", "")
    for character in plain_text:
        if character.isalnum():
            if character.isdigit():
                encode += character
            else:
                if character.isupper():
                    index = plain.find(character.lower())
                    encode += cipher[index]
                else:
                    index = plain.find(character)
                    encode += cipher[index]

    return ' '.join(encode[i:i + 5] for i in range(0, len(encode), 5))


def decode(ciphered_text):
    decode = ''
    ciphered_text = ciphered_text.replace(" ", "")
    for character in ciphered_text:
        if character.isdigit():
            decode += character
        else:
            index = plain.find(character)
            decode += cipher[index]
    return decode