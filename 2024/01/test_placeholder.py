import pytest

from placeholder import calculate_placeholder


test_result_a = 0
test_result_b = 0

lines = []


@pytest.fixture(autouse=True)
def load_lines():
    global lines
    with open("./input1.txt", "r") as f:
        lines = f.readlines()


def test_placeholder():
    assert calculate_placeholder(lines) == test_result_a


# def test_placeholder2():
#     assert calculate_placeholder2(lines) == test_result_b
