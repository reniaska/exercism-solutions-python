# https://exercism.org/tracks/python/exercises/flatten-array

def flatten(iterable):
    if len(iterable) == 0:
        return iterable
    if type(iterable[0]) == list:
        return flatten(iterable[0]) + flatten(iterable[1:])
    elif iterable[0] is not None:
        return iterable[:1] + flatten(iterable[1:])
    return flatten(iterable[1:])
