import pytest

from strength import calculate_strength

test_result_a = 13140

lines = []


@pytest.fixture(autouse=True)
def load_lines():
    global lines
    with open('./input1.txt', 'r') as f:
        lines = f.readlines()


def test_strength():
    assert calculate_strength(lines) == test_result_a
