import pytest

from score import calculate_score
from outcome import calculate_outcome

test_result_a = 15
test_result_b = 12

lines = []


@pytest.fixture(autouse=True)
def load_lines():
    global lines
    with open('./input1.txt', 'r') as f:
        lines = f.readlines()


def test_score():
    assert calculate_score(lines) == test_result_a


def test_outcome():
    assert calculate_outcome(lines) == test_result_b
