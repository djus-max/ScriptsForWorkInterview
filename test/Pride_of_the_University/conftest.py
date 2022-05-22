import pytest
import json
from faker import Faker
import random

fake = Faker(['en_US'])


@pytest.fixture
def load_data():
    students_avg_scores = {
        'Max': 4.964,
        'Eric': 4.962,
        'Peter': 4.923,
        'Mark': 4.957,
        'Julie': 4.95,
        'Jimmy': 4.973,
        'Felix': 4.937,
        'Vasya': 4.911,
        'Don': 4.936,
        'Zoi': 4.937
    }
    return students_avg_scores
