import pytest

from rest import calculate_rest
from floor import calculate_floor

test_result_a = 24
test_result_b = 93

lines = []


@pytest.fixture(autouse=True)
def load_lines():
    global lines
    with open('./input1.txt', 'r') as f:
        lines = f.readlines()


def test_sand():
    assert calculate_rest(lines) == test_result_a


def test_floor():
    assert calculate_floor(lines) == test_result_b
