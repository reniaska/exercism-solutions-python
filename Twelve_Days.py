# https://exercism.org/tracks/python/exercises/twelve-days

DAYS = ('first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh',
        'eighth', 'ninth', 'tenth', 'eleventh', 'twelfth')
GIFTS = ('a Partridge in a Pear Tree.', 'two Turtle Doves, and',
         'three French Hens,', 'four Calling Birds,', 'five Gold Rings,',
         'six Geese-a-Laying,', 'seven Swans-a-Swimming,', 'eight Maids-a-Milking,',
         'nine Ladies Dancing,',  'ten Lords-a-Leaping,',  'eleven Pipers Piping,',
         'twelve Drummers Drumming,')


def verse_gifts(verse):
    if verse == 1:
        return GIFTS[0]
    return GIFTS[verse - 1] + " " + verse_gifts(verse - 1)


def recite(start_verse, end_verse):
    text = "On the {d} day of Christmas my true love gave to me: "
    return [text.format(d=DAYS[day - 1]) + verse_gifts(day) for day in range(start_verse, end_verse + 1)]
