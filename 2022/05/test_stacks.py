import pytest

from topstack import calculate_tops
from multistack import calculate_multi_tops

test_result_a = 'CMZ'
test_result_b = 'MCD'

lines = []


@pytest.fixture(autouse=True)
def load_lines():
    global lines
    with open('./input1.txt', 'r') as f:
        lines = f.readlines()


def test_top():
    assert calculate_tops(lines) == test_result_a


def test_multi():
    assert calculate_multi_tops(lines) == test_result_b
