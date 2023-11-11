#https://exercism.org/tracks/python/exercises/anagram

def find_anagrams(word, candidates):
    return [voc for voc in candidates if sorted(voc.lower()) ==
            sorted(word.lower()) and voc.lower() != word.lower()]

