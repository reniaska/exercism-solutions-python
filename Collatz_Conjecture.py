#https://exercism.org/tracks/python/exercises/collatz-conjecture

def steps(number):
    num_steps = 0
    if number > 0 and isinstance(number, int):
        while number != 1:
            if number % 2 == 0:
                number = number / 2
            else:
                number = 3 * number + 1
            num_steps += 1
        return num_steps
    else:
        raise ValueError("Only positive integers are allowed")