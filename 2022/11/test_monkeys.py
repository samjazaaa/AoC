import pytest

from business import calculate_business
from worry import calculate_worry

test_result_a = 10605
test_result_b = 2713310158

lines = []


@pytest.fixture(autouse=True)
def load_lines():
    global lines
    with open('./input1.txt', 'r') as f:
        lines = f.readlines()


def test_business():
    assert calculate_business(lines) == test_result_a


def test_worry():
    assert calculate_worry(lines) == test_result_b
