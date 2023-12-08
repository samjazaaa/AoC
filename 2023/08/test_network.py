import pytest

from count import calculate_count
from parallel import calculate_parallel


test_result_a = 2
test_result_b = 6

lines = []
extra = []


@pytest.fixture(autouse=True)
def load_lines():
    global lines, extra
    with open("./input1.txt", "r") as f:
        lines = f.readlines()
    with open("./input3.txt", "r") as f:
        extra = f.readlines()


def test_count():
    assert calculate_count(lines) == test_result_a


def test_parallel():
    assert calculate_parallel(extra) == test_result_b
