#https://exercism.org/tracks/python/exercises/prime-factors

def is_prime(number):
    if number <= 1:
        return False
    for factor in range(2, (int(number ** 0.5)) + 1):
        if number % factor == 0:
            return False
    return True


def is_prime_factor(number, factor):
    if is_prime(factor) and number % factor == 0:
        return True
    return False


def factors(value):
    prime_factors = []
    while value > 1:
        for factor in range(2, value + 1):
            if is_prime_factor(value, factor):
                prime_factors.append(factor)
                value //= factor
                break
    return prime_factors