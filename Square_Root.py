# https://exercism.org/tracks/python/exercises/square-root

def square_root(number):
    result = 0
    for num in range(number+1):
        if num*num == number:
            result = num
            break
    return result
