# https://exercism.org/tracks/python/exercises/resistor-color-expert

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

tolerance = {"grey": '0.05%',
             "violet": '0.1%',
             "blue": '0.25%',
             "green": '0.5%',
             "brown": '1%',
             "red": '2%',
             "gold": '5%',
             "silver": '10%'}


def resistor_label(colors):
    if len(colors) == 1:
        return "0 ohms"
    else:
        if len(colors) == 4:
            ohms = (10 * res_colors[colors[0]] + res_colors[colors[1]]) * (10 ** res_colors[colors[2]])
        else:
            ohms = (100 * res_colors[colors[0]] + 10 * res_colors[colors[1]] + res_colors[colors[2]]) * (
                        10 ** res_colors[colors[3]])

    res_tolerance = tolerance[colors[-1]]
    if ohms >= 1000000000:
        ohms /= 1000000000
        prefix = 'giga'
    elif ohms >= 1000000:
        ohms /= 1000000
        prefix = 'mega'
    elif ohms >= 1000:
        ohms /= 1000
        prefix = 'kilo'
    else:
        prefix = ""
    return f"{ohms:n} {prefix}ohms ±{res_tolerance}"
