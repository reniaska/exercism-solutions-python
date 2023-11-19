# https://exercism.org/tracks/python/exercises/luhn

class Luhn:

    def __init__(self, card_num):
        self.card_num = card_num

    def valid(self):
        card_num = self.card_num.replace(' ', '')
        if len(card_num) <= 1 or not card_num.replace(' ', '').isdigit():
            return False
        num_list = [int(num) for num in card_num]
        num_list[-2::-2] = [2 * num if num < 5 else 2 * num - 9 for num in num_list[-2::-2]]
        return sum(num_list) % 10 == 0
