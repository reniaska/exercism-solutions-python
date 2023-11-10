#https://exercism.org/tracks/python/exercises/nth-prime

def prime(number):
    if number == 0:
        raise ValueError('there is no zeroth prime')
    if number < 0:
        raise ValueError('Input must be 1 or greater.')

    num = 1
    while number > 0:
        num += 1
        if is_prime(num):
            number -= 1
    return num


def is_prime(number):
    if number <= 1:
        return False
    for factor in range(2, (int(number ** 0.5)) + 1):
        if number % factor == 0:
            return False
    return True