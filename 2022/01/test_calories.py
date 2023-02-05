import pytest

from maxCalories import max_calories
from topCalories import top_calories

test_result_a = 24000
test_result_b = 45000

lines = []


@pytest.fixture(autouse=True)
def load_lines():
    global lines
    with open('./input1.txt', 'r') as f:
        lines = f.readlines()


def test_max():
    assert max_calories(lines) == test_result_a


def test_top():
    assert top_calories(lines) == test_result_b
