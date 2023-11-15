#https://exercism.org/tracks/python/exercises/say

ones = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten',
        'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen',
        'sixteen', 'seventeen', 'eighteen', 'ninteen']
tens = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty',
    'seventy', 'eighty', 'ninety']


def say(number):
    if number > 999999999999 or number < 0:
        raise ValueError("input out of range")
    if number < 20:
        return ones[number]
    if number < 100:
        rest = number % 10
        return tens[number // 10] + ('-' + ones[rest] if rest != 0 else '')
    if number < 1000:
        rest = number % 100
        return ones[number // 100] + ' hundred' + (' ' + say(rest) if rest != 0 else '')
    if number < 1000000:
        rest = number % 1000
        return say(number // 1000) + ' thousand' + (' ' + say(rest) if rest != 0 else '')
    if number < 1000000000:
        rest = number % 1000000
        return say(number // 1000000) + ' million' + (' ' + say(rest) if rest != 0 else '')
    if number < 1000000000000:
        rest = number % 1000000000
        return say(number // 1000000000) + ' billion' + (' ' + say(rest) if rest != 0 else '')