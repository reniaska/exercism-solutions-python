# https://exercism.org/tracks/python/exercises/bob

def response(hey_bob):
    if hey_bob.isspace() or len(hey_bob) == 0:
        return "Fine. Be that way!"
    elif hey_bob.rstrip()[-1] == '?':
        if hey_bob.isupper():
            return "Calm down, I know what I'm doing!"
        else:
            return 'Sure.'
    elif hey_bob.isupper():
        return "Whoa, chill out!"
    else:
        return 'Whatever.'
