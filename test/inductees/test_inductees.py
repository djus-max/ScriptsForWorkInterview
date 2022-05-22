import pytest
from inductees.inductees import get_inductees


class Test_get_inductees():

    def test_get_inductees(self, load_data):
        names, birthday_years, genders = load_data
        inductees, inaccurate_data = get_inductees(names, birthday_years, genders)
        assert len(inductees) == 1
        assert len(inaccurate_data) == 8
