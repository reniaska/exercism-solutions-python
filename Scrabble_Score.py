#https://exercism.org/tracks/python/exercises/scrabble-score

LETTER_VALUES = {"AEIOULNRST": 1,
                 "DG": 2,
                 "BCMP": 3,
                 "FHVWY": 4,
                 "K": 5,
                 "JX": 8,
                 "QZ": 10}


def score(word):
    points = 0
    for letter in word.lower():
        for key in LETTER_VALUES:
            if letter in key.lower():
                points += LETTER_VALUES[key]
    return points