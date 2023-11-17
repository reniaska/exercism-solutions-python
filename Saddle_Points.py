# https://exercism.org/tracks/python/exercises/saddle-points

def saddle_points(matrix):
    result = []
    for idx_row, row in enumerate(matrix):
        if len(row) != len(matrix[0]):
            raise ValueError('irregular matrix')
        for idx_col, col in enumerate(zip(*matrix)):
            if max(row) == min(col):
                result.append({"row": idx_row + 1, "column": idx_col + 1})
    return result
