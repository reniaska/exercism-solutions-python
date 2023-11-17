# https://exercism.org/tracks/python/exercises/perfect-numbers

def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    divisors_sum = 0
    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")
    else:
        for i in range(1, number):
            if number % i == 0:
                divisors_sum += i
        if divisors_sum == number:
            return 'perfect'
        if divisors_sum > number:
            return 'abundant'
        else:
            return 'deficient'
