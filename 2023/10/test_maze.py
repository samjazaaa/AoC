import pytest

from farthest import calculate_farthest

# from backwards import calculate_backwards


test_result_a = 8
# test_result_b = 2

lines = []


@pytest.fixture(autouse=True)
def load_lines():
    global lines, extra
    with open("./input1.txt", "r") as f:
        lines = f.readlines()


def test_farthest():
    assert calculate_farthest(lines) == test_result_a


# def test_backwards():
#     assert calculate_backwards(lines) == test_result_b
