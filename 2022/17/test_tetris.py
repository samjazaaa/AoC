import pytest

from drop import calculate_drop

test_result_a = 3068

lines = []


@pytest.fixture(autouse=True)
def load_lines():
    global lines
    with open('./input1.txt', 'r') as f:
        lines = f.readlines()


def test_drop():
    assert calculate_drop(lines) == test_result_a
