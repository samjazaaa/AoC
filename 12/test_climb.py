import pytest

from shortest import calculate_shortest
from scenic import calculate_scenic

test_result_a = 31
test_result_b = 29

lines = []


@pytest.fixture(autouse=True)
def load_lines():
    global lines
    with open('./input1.txt', 'r') as f:
        lines = f.readlines()


def test_shortest():
    assert calculate_shortest(lines) == test_result_a


def test_scenic():
    assert calculate_scenic(lines) == test_result_b
