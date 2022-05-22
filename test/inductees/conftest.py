import pytest
import json
from faker import Faker
import random

fake = Faker(['en_US'])


@pytest.fixture
def load_data():
    names = ["Vasya", "Alice", "Petya", "Jenny", "Fedya", "Viola", "Mark", "Chris", "Margo"]
    birthday_years = [1962, 1995, 2000, None, None, None, None, 1998, 2001]
    genders = ["Male", "Female", "Male", "Female", "Male", None, None, None, None]

    return names, birthday_years, genders
