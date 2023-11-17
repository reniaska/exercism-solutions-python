# https://exercism.org/tracks/python/exercises/pythagorean-triplet

def triplets_with_sum(number):
    triangles = []
    for a in range(1, number // 3):
        for b in range(a, (number - a) // 2 + 1):
            c = number - a - b
            if a * a + b * b == c * c:
                triangles.append(sorted([a, b, c]))
    return triangles
