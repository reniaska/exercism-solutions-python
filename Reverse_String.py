#https://exercism.org/tracks/python/exercises/reverse-string

def reverse(text):
    reverse_str = ''
    for i in range(1, len(text) + 1):
        reverse_str += text[-i]
    return reverse_str
