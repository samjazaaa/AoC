import pytest

from antinodes import calculate_antinodes
from resonance import calculate_resonance


test_result_a = 14
test_result_b = 34

lines = []


@pytest.fixture(autouse=True)
def load_lines():
    global lines
    with open("./input1.txt", "r") as f:
        lines = f.readlines()


def test_antinodes():
    assert calculate_antinodes(lines) == test_result_a


def test_resonance():
    assert calculate_resonance(lines) == test_result_b
