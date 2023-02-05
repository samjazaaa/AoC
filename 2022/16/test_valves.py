import pytest

from pressure import calculate_pressure

test_result_a = 1651

lines = []


@pytest.fixture(autouse=True)
def load_lines():
    global lines
    with open('./input1.txt', 'r') as f:
        lines = f.readlines()


def test_pressure():
    assert calculate_pressure(lines) == test_result_a
