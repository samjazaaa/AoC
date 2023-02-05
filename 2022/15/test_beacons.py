import pytest

from coverage import calculate_coverage
from frequency import calculate_frequency

test_result_a = 26
test_result_b = 56000011

lines = []


@pytest.fixture(autouse=True)
def load_lines():
    global lines
    with open('./input1.txt', 'r') as f:
        lines = f.readlines()


def test_coverage():
    assert calculate_coverage(lines) == test_result_a


def test_floor():
    assert calculate_frequency(lines) == test_result_b
