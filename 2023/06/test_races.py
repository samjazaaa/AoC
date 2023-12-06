import pytest

from possibilities import calculate_possibilities

from combined import calculate_combined


test_result_a = 288
test_result_b = 71503

lines = []


@pytest.fixture(autouse=True)
def load_lines():
    global lines
    with open("./input1.txt", "r") as f:
        lines = f.readlines()


def test_possibilities():
    assert calculate_possibilities(lines) == test_result_a


def test_combined():
    assert calculate_combined(lines) == test_result_b
