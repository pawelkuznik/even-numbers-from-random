import pytest
from even_number_from_random import EvenNumberFromRandom



class TestEvenNumberFromRandom:

    @pytest.fixture()
    def resource(self):
        obj = EvenNumberFromRandom(0, 1000, 10)
        obj.random_list_numbers()
        return obj.even_list_numbers()
#       return [0, 1, 2]

    def test_if_even_list_is_not_empty(self, resource):
        assert resource

    def test_if_even_list_contain_only_evens(self, resource):
        my_list = [num for num in resource if num % 2 == 0]
        assert len(resource) == len(my_list)

    def test_if_even_list_contain_only_odds(self, resource):
        # resource = [1, 3, 5]
        my_list = [num for num in resource if num % 2 == 0]
        assert my_list

    def test_if_even_list_contain_even_and_odd_numbers(self, resource):
        even_list = [num for num in resource if num % 2 == 0]
        odd_list = [num for num in resource if num % 2 == 1]
        assert not (even_list and odd_list)
