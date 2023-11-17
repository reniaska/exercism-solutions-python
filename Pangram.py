# https://exercism.org/tracks/python/exercises/pangram

def is_pangram(sentence):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    sentence = sentence.lower()
    letters_sum = 0
    for i in letters:
        count = sentence.count(i)
        if count >= 1:
            letters_sum += 1

    return len(letters) == letters_sum
