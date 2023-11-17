# https://exercism.org/tracks/python/exercises/isbn-verifier

def is_valid(isbn):
    isbn = isbn.replace('-', '')
    formula_sum = 0
    decrement = 0
    if len(isbn) == 10 and isbn[:9].isdigit() and (isbn[9].isdigit() or isbn[9] == 'X'):
        for i in isbn[:9]:
            formula_sum += int(i) * (10-decrement)
            decrement += 1
        if isbn[9] == 'X':
            formula_sum += 10
        else:
            formula_sum += int(isbn[9])
        return formula_sum % 11 == 0
    return False
