# https://exercism.org/tracks/python/exercises/pop-count

def egg_count(display_value):
    counter = 0
    while display_value > 0:
        counter += display_value % 2
        display_value = display_value // 2

    return counter
