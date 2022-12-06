import pytest

from marker import calculate_marker
from message import calculate_message

test_result_a = 10
test_result_b = 29

lines = []


@pytest.fixture(autouse=True)
def load_lines():
    global lines
    with open('./input1.txt', 'r') as f:
        lines = f.readlines()


def test_marker():
    assert calculate_marker(lines) == test_result_a


def test_multi():
    assert calculate_message(lines) == test_result_b
