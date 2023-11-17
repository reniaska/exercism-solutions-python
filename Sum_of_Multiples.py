# https://exercism.org/tracks/python/exercises/sum-of-multiples

def sum_of_multiples(limit, multiples):
    energy_points = []
    for multiple in multiples:
        if multiple != 0:
            for i in range(multiple, limit, multiple):
                energy_points.append(i)
    set_points = set(energy_points)
    return sum(set_points)
