import pytest

from smaller_folders import calculate_dirs
from delete_folder import calculate_delete

test_result_a = 95437
test_result_b = 24933642

lines = []


@pytest.fixture(autouse=True)
def load_lines():
    global lines
    with open('./input1.txt', 'r') as f:
        lines = f.readlines()


def test_smaller():
    assert calculate_dirs(lines) == test_result_a


def test_delete():
    assert calculate_delete(lines) == test_result_b
