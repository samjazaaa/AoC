import pytest

from lock import calculate_zeroes
from track import track_zeroes


test_result_a = 3
test_result_b = 6

lines = []


@pytest.fixture(autouse=True)
def load_lines():
    global lines
    with open("./input1.txt", "r") as f:
        lines = f.readlines()


def test_zeroes():
    assert calculate_zeroes(lines) == test_result_a


def test_track():
    assert track_zeroes(lines) == test_result_b
