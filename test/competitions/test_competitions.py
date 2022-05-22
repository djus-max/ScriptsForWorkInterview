import pytest
from competitions.competitions import find_athlets


class Test_find_athlets():

    def test_find_athlets(self, load_data):
        know_english, sportsmen, more_than_20_years = load_data
        athlets = find_athlets(know_english, sportsmen, more_than_20_years)
        assert len(athlets) == 2
