import pytest

from extrapolate import calculate_extrapolation

from backwards import calculate_backwards


test_result_a = 114
test_result_b = 2

lines = []


@pytest.fixture(autouse=True)
def load_lines():
    global lines, extra
    with open("./input1.txt", "r") as f:
        lines = f.readlines()


def test_extrapolation():
    assert calculate_extrapolation(lines) == test_result_a


def test_backwards():
    assert calculate_backwards(lines) == test_result_b
