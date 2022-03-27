import random


class EvenNumberFromRandom:
    min_range = 0
    max_range = 0
    amount_numbers = 0
    random_list = []
    even_list = []

    def __init__(self, min_range, max_range, amount_numbers):
        self.min_range = min_range
        self.max_range = max_range
        self.amount_numbers = amount_numbers

    def random_list_numbers(self):
        """
        :arg
        - min_range: integer
        - max_range: integer
        - amount_numbers: integer
        :return
        - list of random unique integers from a range
        """
        self.random_list = random.sample(range(self.min_range, self.max_range), self.amount_numbers)
        print(self.random_list)
        return self.random_list

    def even_list_numbers(self):
        """
        :arg
        - list of random integers
        :return
        - list of even integers
        """
        self.even_list = [num for num in self.random_list if num % 2 == 0]
        print(self.even_list)
        return self.even_list


obj = EvenNumberFromRandom(0, 1000, 10)
obj.random_list_numbers()
obj.even_list_numbers()