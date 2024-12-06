import pytest

from visited import calculate_visited
from loop import calculate_loop


test_result_a = 41
test_result_b = 6

lines = []


@pytest.fixture(autouse=True)
def load_lines():
    global lines
    with open("./input1.txt", "r") as f:
        lines = f.readlines()


def test_visited():
    assert calculate_visited(lines) == test_result_a


def test_loop():
    assert calculate_loop(lines) == test_result_b
