# https://exercism.org/tracks/python/exercises/roman-numerals

ROMAN_NUMERALS = {1000: 'M',
                  500: 'D',
                  100: 'C',
                  50: 'L',
                  10: 'X',
                  5: 'V',
                  1: 'I'}


def roman(number):
    roman_num = ''
    while number > 0:
        for key in ROMAN_NUMERALS:
            print(number, key)
            if number >= key:
                roman_num += ROMAN_NUMERALS[key]
                number -= key
                break
            elif str(number)[0] == '9' and number >= key - (key / 10):
                roman_num += ROMAN_NUMERALS[int(key / 10)] + ROMAN_NUMERALS[key]
                number -= key - (key / 10)
                break
            elif str(number)[0] == '4' and number >= key - 2 * (key / 10):
                roman_num += ROMAN_NUMERALS[int(2 * (key / 10))] + ROMAN_NUMERALS[key]
                number -= key - 2 * (key / 10)
                break
    return roman_num
