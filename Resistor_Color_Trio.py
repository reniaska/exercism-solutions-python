#https://exercism.org/tracks/python/exercises/resistor-color-trio

res_colors = {"black": 0,
              "brown": 1,
              "red": 2,
              "orange": 3,
              "yellow": 4,
              "green": 5,
              "blue": 6,
              "violet": 7,
              "grey": 8,
              "white": 9}


def label(colors):
    ohms = (10 * res_colors[colors[0]] + res_colors[colors[1]]) * (10 ** res_colors[colors[2]])
    if ohms >= 1000000000:
        return str(ohms // 1000000000) + " gigaohms"
    if ohms >= 1000000:
        return str(ohms // 1000000) + " megaohms"
    if ohms >= 1000:
        return str(ohms // 1000) + " kiloohms"
    return str(ohms) + " ohms"