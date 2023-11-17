# https://exercism.org/tracks/python/exercises/sieve

def primes(limit):
    numbers = set(range(2, limit + 1))
    multiplication_list = []
    for num in range(2, int(limit ** 0.5) + 1):
        multiplication = 2
        while num * multiplication <= limit:
            multiplication_list.append(num * multiplication)
            multiplication += 1
    return list(numbers.difference(multiplication_list))
