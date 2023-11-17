# https://exercism.org/tracks/python/exercises/ocr-numbers

DIGITS = [[" _ ", "| |", "|_|", "   "],  #0
          ["   ", "  |", "  |", "   "],  #1
          [" _ ", " _|", "|_ ", "   "],  #2
          [" _ ", " _|", " _|", "   "],  #3
          ["   ", "|_|", "  |", "   "],  #4
          [" _ ", "|_ ", " _|", "   "],  #5
          [" _ ", "|_ ", "|_|", "   "],  #6
          [" _ ", "  |", "  |", "   "],  #7
          [" _ ", "|_|", "|_|", "   "],  #8
          [" _ ", "|_|", " _|", "   "]]  #9


def convert_single_digit(single_grid):
    if single_grid in DIGITS:
        return str(DIGITS.index(single_grid))
    return '?'


def convert(input_grid):
    if len(input_grid) % 4 != 0:
        raise ValueError("Number of input lines is not a multiple of four")
    for line in input_grid:
        if len(line) % 3 != 0:
            raise ValueError("Number of input columns is not a multiple of three")

    result = ''
    for digits_line in range(0, len(input_grid), 4):
        print(digits_line)
        for column in range(0, len(input_grid[0]), 3):
            digit = []
            for row in range(digits_line, digits_line + 4):
                digit.append(input_grid[row][column: column + 3])
            result += convert_single_digit(digit)
        if digits_line < len(input_grid) - 4:
            result += ','
    return result
