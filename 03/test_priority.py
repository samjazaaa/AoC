import pytest

from priority import calculate_priority
from group import calculate_group

test_result_a = 157
test_result_b = 70

lines = []


@pytest.fixture(autouse=True)
def load_lines():
    global lines
    with open('./input1.txt', 'r') as f:
        lines = f.readlines()


def test_priority():
    assert calculate_priority(lines) == test_result_a


def test_outcome():
    assert calculate_group(lines) == test_result_b
