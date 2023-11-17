# https://exercism.org/tracks/python/exercises/armstrong-numbers

def is_armstrong_number(number):
    digits_sum = 0
    digits = len(str(number))
    for num in str(number):
        digits_sum += int(num) ** digits
    return number == digits_sum
