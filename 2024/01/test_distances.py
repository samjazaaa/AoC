import pytest

from distances import calculate_distances
from similarity import calculate_similarity


test_result_a = 11
test_result_b = 31

lines = []


@pytest.fixture(autouse=True)
def load_lines():
    global lines
    with open("./input1.txt", "r") as f:
        lines = f.readlines()


def test_distances():
    assert calculate_distances(lines) == test_result_a


def test_similarity():
    assert calculate_similarity(lines) == test_result_b
