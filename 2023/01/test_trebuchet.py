import pytest

from calibration import calculate_calibration
from letters import calculate_letters


test_result_a = 142
test_result_b = 142

lines = []


@pytest.fixture(autouse=True)
def load_lines():
    global lines
    with open('./input1.txt', 'r') as f:
        lines = f.readlines()


def test_calibration():
    assert calculate_calibration(lines) == test_result_a


def test_scenic():
    assert calculate_letters(lines) == test_result_b
