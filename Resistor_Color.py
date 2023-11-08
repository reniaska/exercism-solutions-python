#https://exercism.org/tracks/python/exercises/resistor-color

resistors_colors = {"black" : 0,
                    "brown" : 1,
                    "red" : 2,
                    "orange" : 3,
                    "yellow" : 4,
                    "green" : 5,
                    "blue" : 6,
                    "violet" : 7,
                    "grey" : 8,
                    "white" : 9}


def color_code(color):
    return resistors_colors[color]


def colors():
    return list(resistors_colors)