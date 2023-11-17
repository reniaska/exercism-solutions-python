# https://exercism.org/tracks/python/exercises/hamming

def distance(strand_a, strand_b):
    dist = 0
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")
    return sum(letter_a != letter_b for letter_a, letter_b in zip(strand_a, strand_b))
