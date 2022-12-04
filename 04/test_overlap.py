import pytest

from contain import calculate_contains
from overlap import calculate_overlap

test_result_a = 2
test_result_b = 4

lines = []


@pytest.fixture(autouse=True)
def load_lines():
    global lines
    with open('./input1.txt', 'r') as f:
        lines = f.readlines()


def test_contains():
    assert calculate_contains(lines) == test_result_a


def test_overlap():
    assert calculate_overlap(lines) == test_result_b
