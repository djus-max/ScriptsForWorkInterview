import pytest


@pytest.fixture
def load_data():
    know_english = ["Vasya", "Jimmy", "Max", "Peter", "Eric", "Zoi", "Felix"]
    sportsmen = ["Don", "Peter", "Eric", "Jimmy", "Mark"]
    more_than_20_years = ["Peter", "Julie", "Jimmy", "Mark", "Max"]

    return know_english, sportsmen, more_than_20_years
