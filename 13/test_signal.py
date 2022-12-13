import pytest

from order import calculate_order
from decoder import calculate_decoder

test_result_a = 13
test_result_b = 140

lines = []


@pytest.fixture(autouse=True)
def load_lines():
    global lines
    with open('./input1.txt', 'r') as f:
        lines = f.readlines()


def test_order():
    assert calculate_order(lines) == test_result_a


def test_decoder():
    assert calculate_decoder(lines) == test_result_b
