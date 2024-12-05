import pytest

from order import calculate_order
from sort import calculate_sort


test_result_a = 143
test_result_b = 123

lines = []


@pytest.fixture(autouse=True)
def load_lines():
    global lines
    with open("./input1.txt", "r") as f:
        lines = f.readlines()


def test_order():
    assert calculate_order(lines) == test_result_a


def test_sort():
    assert calculate_sort(lines) == test_result_b
