import pytest

from safe import calculate_safe
from fix import calculate_fixed


test_result_a = 2
test_result_b = 4

lines = []


@pytest.fixture(autouse=True)
def load_lines():
    global lines
    with open("./input1.txt", "r") as f:
        lines = f.readlines()


def test_safe():
    assert calculate_safe(lines) == test_result_a


def test_fixed():
    assert calculate_fixed(lines) == test_result_b
