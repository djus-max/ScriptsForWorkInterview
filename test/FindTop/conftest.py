import pytest
import json
from faker import Faker
import random

fake = Faker(['en_US'])


@pytest.fixture
def identical_data(len_data):
    """ идентичные данные """
    data = []
    count = 0
    while len_data > count:
        item = {
            "name": fake.name(),
            "scores": {
                "math": 70,
                "russian_language": 70,
                "computer_science": 70
            },
            "extra_scores": random.randrange(1)
        }
        data.append(item)
        count += 1

    return data


@pytest.fixture
def identical_data_step(len_data, step=3):
    """ идентичные данные """
    step = step
    data = []
    count = 0
    while len_data > count:
        if count % step == 0:
            flag = True
            if count % 2 == 0:
                c = 2
            else:
                c = 1
        else:
            flag = False
        item = {
            "name": fake.name(),
            "scores": {
                "math": 70,
                "russian_language": 70,
                "computer_science": 70
            },
            "extra_scores": random.randrange(1) if not flag else c
        }
        data.append(item)
        count += 1

    return data


@pytest.fixture
def load_data():
    with open('FindTop/candidates.json', 'r') as f:
        candidates = json.load(f)

    return candidates
