import pytest

from possible import calculate_possible

from power import calculate_power


test_result_a = 8
test_result_b = 2286

lines = []


@pytest.fixture(autouse=True)
def load_lines():
    global lines
    with open("./input1.txt", "r") as f:
        lines = f.readlines()


def test_calibration():
    assert calculate_possible(lines) == test_result_a


def test_power():
    assert calculate_power(lines) == test_result_b
