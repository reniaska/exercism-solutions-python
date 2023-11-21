# https://exercism.org/tracks/python/exercises/robot-simulator
# Globals for the directions
# Change the values as you see fit
EAST = (1, 0)
NORTH = (0, 1)
WEST = (-1, 0)
SOUTH = (0, -1)

DIRECTIONS = [NORTH, EAST, SOUTH, WEST]


class Robot:
    def __init__(self, direction=NORTH, x_pos=0, y_pos=0):
        self.direction = direction
        self.coordinates = (x_pos, y_pos)

    def move(self, instructions=''):
        for instruction in instructions:
            index = DIRECTIONS.index(self.direction)
            if instruction == 'R':
                self.direction = DIRECTIONS[(index + 1) % 4]
            elif instruction == 'L':
                self.direction = DIRECTIONS[index - 1]
            elif instruction == 'A':
                self.coordinates = tuple(map(sum, zip(self.coordinates, self.direction)))
            else:
                # if an instruction is different to R, L or A
                raise ValueError("instruction doesn't exist")
