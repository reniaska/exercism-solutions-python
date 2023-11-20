# https://exercism.org/tracks/python/exercises/robot-name/

import random

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


class Robot:
    existing_names = list()

    def __init__(self):
        name = self.give_name()
        while name in self.existing_names:
            name = self.give_name()
        self.name = name
        self.existing_names.append(name)

    def reset(self):
        self.__init__()
        self.existing_names.remove(self.name)

    @staticmethod
    def give_name():
        name_letters = ''.join([random.choice(LETTERS) for i in range(2)])
        name_numbers = ''.join([str(random.randint(0, 9)) for i in range(3)])
        return name_letters + name_numbers
