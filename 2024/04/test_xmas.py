import pytest

from find import calculate_find
from cross import calculate_cross


test_result_a = 18
test_result_b = 9

lines = []


@pytest.fixture(autouse=True)
def load_lines():
    global lines
    with open("./input1.txt", "r") as f:
        lines = f.readlines()


def test_find():
    assert calculate_find(lines) == test_result_a


def test_cross():
    assert calculate_cross(lines) == test_result_b
