import pytest

from mul import calculate_mul
from conditional import calculate_conditional


test_result_a = 161
test_result_b = 48

lines = []


@pytest.fixture(autouse=True)
def load_lines():
    global lines
    with open("./input1.txt", "r") as f:
        lines = f.readlines()


def test_mul():
    assert calculate_mul(lines) == test_result_a


def test_cond():
    assert calculate_conditional(lines) == test_result_b
