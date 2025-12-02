import pytest

from mirror import calculate_mirrors
from sequence import calculate_sequence


test_result_a = 1227775554
test_result_b = 4174379265

lines = []


@pytest.fixture(autouse=True)
def load_lines():
    global lines
    with open("./input1.txt", "r") as f:
        lines = f.readlines()


def test_mirror():
    assert calculate_mirrors(lines) == test_result_a


def test_sequence():
    assert calculate_sequence(lines) == test_result_b
