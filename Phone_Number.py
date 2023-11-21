# https://exercism.org/tracks/python/exercises/phone-number

import re


class PhoneNumber:
    def __init__(self, number):
        number = self.clean(number)

        if number.isdigit() and len(number) < 10:
            # if a phone number has less than 10 digits.
            raise ValueError("must not be fewer than 10 digits")

        if number.isdigit() and len(number) > 11:
            # if a phone number has more than 11 digits.
            raise ValueError("must not be greater than 11 digits")

        if len(number) == 11:
            if number.isdigit() and number[0] != '1':
                # if a phone number has 11 digits, but starts with a number other than 1.
                raise ValueError("11 digits must start with 1")
            number = number[1:]

        area_code = number[:3]

        if area_code[0] == '0':
            # if a phone number has an area code that starts with 0.
            raise ValueError("area code cannot start with zero")

        if area_code[0] == '1':
            # if a phone number has an area code that starts with 1.
            raise ValueError("area code cannot start with one")

        exchange_code = number[3:6]

        if exchange_code[0] == '0':
            # if a phone number has an exchange code that starts with 0.
            raise ValueError("exchange code cannot start with zero")

        if exchange_code[0] == '1':
            # if a phone number has an exchange code that starts with 1.
            raise ValueError("exchange code cannot start with one")

        if re.findall(r'[^a-zA-Z0-9]', number):
            # if a phone number has punctuation in place of some digits.
            raise ValueError("punctuations not permitted")

        if re.findall(r'[a-zA-Z]', number):
            # if a phone number has letters in place of some digits.
            raise ValueError("letters not permitted")

        self.exchange_code = exchange_code
        self.area_code = area_code
        self.subscriber_number = number[6:]
        self.number = number

    @staticmethod
    def clean(number):
        result = re.sub(r'[+()\-.\s]', '', number)
        return result

    def pretty(self):
        return '(' + self.area_code + ')-' + self.exchange_code + '-' + self.subscriber_number
