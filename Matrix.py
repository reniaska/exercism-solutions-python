# https://exercism.org/tracks/python/exercises/matrix

class Matrix:
    def __init__(self, matrix_string):
        self.matrix = [[int(num) for num in row.split()] for row in matrix_string.split('\n')]

    def row(self, index):
        return self.matrix[index - 1]

    def column(self, index):
        columns = list(zip(*self.matrix))
        return list(columns[index - 1])
