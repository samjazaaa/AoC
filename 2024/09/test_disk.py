import pytest

from compact import calculate_compact


test_result_a = 1928
test_result_b = 34

lines = []


@pytest.fixture(autouse=True)
def load_lines():
    global lines
    with open("./input1.txt", "r") as f:
        lines = f.readlines()


def test_compact():
    assert calculate_compact(lines) == test_result_a


# def test_resonance():
#     assert calculate_resonance(lines) == test_result_b
