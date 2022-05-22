import json
from faker import Faker
import random

fake = Faker(['en_US'])


def random_data(len_data):
    """ """
    data = []
    count = 0

    while len_data > count:
        item = {
            "name": fake.name(),
            "scores": {
                "math": random.randrange(100),
                "russian_language": random.randrange(100),
                "computer_science": random.randrange(100)
            },
            "extra_scores": random.randrange(10)
        }
        data.append(item)
        count += 1

    return data


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


if __name__ == '__main__':
    data = random_data(len_data=50)

    # data = identical_data_step(len_data=15)

    with open('WebPython/candidates.json', 'w') as f:
        json.dump(data, f, indent=4)
