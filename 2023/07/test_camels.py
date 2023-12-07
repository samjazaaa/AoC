import pytest

from winnings import calculate_winnings

from joker import calculate_joker


test_result_a = 6440
test_result_b = 5905

lines = []


@pytest.fixture(autouse=True)
def load_lines():
    global lines
    with open("./input1.txt", "r") as f:
        lines = f.readlines()


def test_winnings():
    assert calculate_winnings(lines) == test_result_a


def test_joker():
    assert calculate_joker(lines) == test_result_b
