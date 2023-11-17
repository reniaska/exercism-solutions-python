# https://exercism.org/tracks/python/exercises/scrabble-score

letter_values = {"AEIOULNRST": 1,
                 "DG": 2,
                 "BCMP": 3,
                 "FHVWY": 4,
                 "K": 5,
                 "JX": 8,
                 "QZ": 10}


def score(word):
    points = 0
    for letter in word.lower():
        for key in letter_values:
            if letter in key.lower():
                points += letter_values[key]
    return points
