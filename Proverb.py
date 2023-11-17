# https://exercism.org/tracks/python/exercises/proverb

def proverb(*args, qualifier):
    if len(args) == 0:
        return []
    lines = [f"For want of a {w1} the {w2} was lost." for w1, w2 in zip(args, args[1:])]
    if qualifier is None:
        qualifier = ""
    else:
        qualifier += " "
    last_line = f"And all for the want of a {qualifier}{args[0]}."
    return lines + [last_line]
