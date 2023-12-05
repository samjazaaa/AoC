import pytest

from closest import calculate_closest

from ranges import calculate_ranges


test_result_a = 35
test_result_b = 46

lines = []


@pytest.fixture(autouse=True)
def load_lines():
    global lines
    with open("./input1.txt", "r") as f:
        lines = f.readlines()


def test_closest():
    assert calculate_closest(lines) == test_result_a


def test_ranges():
    assert calculate_ranges(lines) == test_result_b
