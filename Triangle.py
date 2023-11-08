#https://exercism.org/tracks/python/exercises/triangle

def equilateral(sides):
    all_positive = sides[0] > 0 and sides[1] > 0 and sides[2] > 0
    possible_to_built = (sides[0] + sides[1] >= sides[2]) and (sides[1] + sides[2] >= sides[0]) and (sides[2] + sides[0] >= sides[1])
    return sides[0] == sides[1] == sides[2] and all_positive and possible_to_built


def isosceles(sides):
    all_positive = sides[0] > 0 and sides[1] > 0 and sides[2] > 0
    possible_to_built = (sides[0] + sides[1] >= sides[2]) and (sides[1] + sides[2] >= sides[0]) and (sides[2] + sides[0] >= sides[1])
    return (sides[0] == sides[1] or sides[1] == sides[2] or sides[0] == sides[2]) and all_positive and possible_to_built


def scalene(sides):
    all_positive = sides[0] > 0 and sides[1] > 0 and sides[2] > 0
    possible_to_built = (sides[0] + sides[1] >= sides[2]) and (sides[1] + sides[2] >= sides[0]) and (sides[2] + sides[0] >= sides[1])
    return (sides[0] != sides[1] and sides[1] != sides[2] and sides[0] != sides[2]) and all_positive and possible_to_built