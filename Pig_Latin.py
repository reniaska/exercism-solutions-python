# https://exercism.org/tracks/python/exercises/pig-latin

def translate_word(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    if text[0] in vowels or text[0:2] in ['xr', 'yt']:
        return text + 'ay'
    else:
        start = 0
        for i in list(text):
            if i in vowels or (text.index(i) > 0 and i == 'y'):
                break
            else:
                start += 1
        word = text[start:] + text[:start]
        if word[0] == 'u' and word[-1] == 'q':
            return word[1:] + word[0] + 'ay'
        return word + 'ay'


def translate(sentence):
    return " ".join([translate_word(word) for word in sentence.split()])
