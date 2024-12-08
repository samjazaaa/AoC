import pytest

from operators import calculate_operators
from concat import calculate_concat


test_result_a = 3749
test_result_b = 11387

lines = []


@pytest.fixture(autouse=True)
def load_lines():
    global lines
    with open("./input1.txt", "r") as f:
        lines = f.readlines()


def test_operators():
    assert calculate_operators(lines) == test_result_a


def test_loop():
    assert calculate_concat(lines) == test_result_b
