import pytest

from visible import calculate_visible
from scenery import calculate_scenery

test_result_a = 21
test_result_b = 8

lines = []


@pytest.fixture(autouse=True)
def load_lines():
    global lines
    with open('./input1.txt', 'r') as f:
        lines = f.readlines()


def test_visible():
    assert calculate_visible(lines) == test_result_a


def test_scenic():
    assert calculate_scenery(lines) == test_result_b
