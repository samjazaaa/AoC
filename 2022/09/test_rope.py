import pytest

from visited import calculate_visited
from long import calculate_long

test_result_a = 13
test_result_b = 1

lines = []


@pytest.fixture(autouse=True)
def load_lines():
    global lines
    with open('./input1.txt', 'r') as f:
        lines = f.readlines()


def test_visited():
    assert calculate_visited(lines) == test_result_a


def test_long():
    assert calculate_long(lines) == test_result_b
