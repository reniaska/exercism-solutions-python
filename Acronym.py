# https://exercism.org/tracks/python/exercises/acronym

def abbreviate(words):
    words = words.replace('-', ' ').replace('_', ' ').split()
    return "".join(word[0].upper() for word in words)
