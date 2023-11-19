# https://exercism.org/tracks/python/exercises/dnd-character

import random


def modifier(constitution):
    return (constitution - 10) // 2


class Character:

    def __init__(self):
        self.strength = self.ability()
        self.dexterity = self.ability()
        self.constitution = self.ability()
        self.intelligence = self.ability()
        self.wisdom = self.ability()
        self.charisma = self.ability()
        self.hitpoints = 10 + modifier(self.constitution)

    @staticmethod
    def ability():
        dices = sorted([random.randint(1, 6) for num in range(4)])
        return sum(dices[1:])
