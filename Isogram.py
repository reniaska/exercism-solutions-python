#https://exercism.org/tracks/python/exercises/isogram

def is_isogram(string):
    string = string.lower()
    letters = 'abcdefghijklmnopqrstuvwxyz'
    for i in string:
        if i in letters:
            count = string.count(i)
            if count > 1:
                return False
    return True