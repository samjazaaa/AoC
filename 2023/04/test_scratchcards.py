import pytest

from winning import calculate_winning

from copies import calculate_copies


test_result_a = 13
test_result_b = 30

lines = []


@pytest.fixture(autouse=True)
def load_lines():
    global lines
    with open("./input1.txt", "r") as f:
        lines = f.readlines()


def test_winning():
    assert calculate_winning(lines) == test_result_a


def test_copies():
    assert calculate_copies(lines) == test_result_b
