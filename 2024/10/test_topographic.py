import pytest

from scores import calculate_scores


test_result_a = 36
test_result_b = 2858

lines = []


@pytest.fixture(autouse=True)
def load_lines():
    global lines
    with open("./input1.txt", "r") as f:
        lines = f.readlines()


def test_scores():
    assert calculate_scores(lines) == test_result_a


# def test_fragmentation():
#     assert calculate_fragmentation(lines) == test_result_b
