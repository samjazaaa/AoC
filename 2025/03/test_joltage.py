import pytest

from joltage import calculate_joltage
from friction import calculate_friction


test_result_a = 357
test_result_b = 3121910778619

lines = []


@pytest.fixture(autouse=True)
def load_lines():
    global lines
    with open("./input1.txt", "r") as f:
        lines = f.readlines()


def test_joltage():
    assert calculate_joltage(lines) == test_result_a


def test_friction():
    assert calculate_friction(lines) == test_result_b
