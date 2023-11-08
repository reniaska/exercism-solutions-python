#https://exercism.org/tracks/python/exercises/grains

def square(number):
    if isinstance(number, int) and (number in range(1, 65)):
        return 2**(number-1)
    else:
        raise ValueError("square must be between 1 and 64")


def total():
    total = 0
    for i in range (1, 65):
        total += square(i)
    return total