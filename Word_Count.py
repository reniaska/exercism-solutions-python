# https://exercism.org/tracks/python/exercises/word-count
import re


def count_words(sentence):
    words = re.findall(r"[a-z0-9]+(?:'[a-z]+)?", sentence.lower())
    return {word: words.count(word) for word in words}
