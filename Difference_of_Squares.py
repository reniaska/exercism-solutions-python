#https://exercism.org/tracks/python/exercises/difference-of-squares

def square_of_sum(number):
    #  using formula (n/2)*(a1+an)
    return ((1 + number) * number // 2) ** 2


def sum_of_squares(number):
    # using formula (n*(n+1)*(2n+1))/6
    return (number * (number + 1) * (2 * number + 1)) // 6


def difference_of_squares(number):
    return square_of_sum(number) - sum_of_squares(number)