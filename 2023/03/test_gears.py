import pytest

from parts import calculate_parts

from ratio import calculate_ratios


test_result_a = 4361
test_result_b = 467835

lines = []


@pytest.fixture(autouse=True)
def load_lines():
    global lines
    with open("./input1.txt", "r") as f:
        lines = f.readlines()


def test_parts():
    assert calculate_parts(lines) == test_result_a


def test_ratios():
    assert calculate_ratios(lines) == test_result_b
