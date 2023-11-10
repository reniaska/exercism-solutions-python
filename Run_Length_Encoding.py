#https://exercism.org/tracks/python/exercises/run-length-encoding

def decode(string):
    num = ''
    result = ''
    for character in string:
        if character.isdigit():
            num += character
        else:
            if len(num) == 0:
                result += character
            else:
                for i in range(0, int(num)):
                    result += character
            num = ''
    return result


def encode(string):
    data = ""
    while len(string) > 0:
        len_before = len(string)
        character = string[0]
        string = string.lstrip(character)
        if len_before - len(string) > 1:
            data += str(len_before - len(string)) + character
        else:
            data += character
    return data