import sys
import math
from functools import cmp_to_key


def compare_rules(val1, val2):
    for rule in rules:
        if rule[0] == val1 and rule[1] == val2:
            return -1
        elif rule[1] == val1 and rule[0] == val2:
            return 1

    return 0


# return all numbers that need to come before val
def get_smaller(val, rules):
    smaller = []

    for rule in rules:
        if rule[1] == val:
            smaller.append(rule[0])

    return smaller


def is_ordered(seq, rules):
    for i, val in enumerate(seq):
        smaller = get_smaller(val, rules)
        for sm in smaller:
            if sm in seq[i:]:
                return False

    return True


def calculate_sort(lines):
    global rules  # yeah, I know
    cleared_lines = []

    for line in lines:
        cleared_lines.append(line.replace("\n", ""))

    # splitt in rules and sequences
    separator = cleared_lines.index("")
    rule_lines = cleared_lines[:separator]
    sequence_lines = cleared_lines[separator + 1 :]

    rules = list(
        map(lambda str: tuple(map(lambda v: int(v), str.split("|"))), rule_lines)
    )

    sequences = list(
        map(lambda str: list(map(lambda v: int(v), str.split(","))), sequence_lines)
    )

    unordered = list(filter(lambda seq: not is_ordered(seq, rules), sequences))

    middle_sum = 0
    for seq in unordered:
        sorted_seq = sorted(seq, key=cmp_to_key(compare_rules))
        middle = math.floor(len(sorted_seq) / 2)
        middle_sum += sorted_seq[middle]

    return middle_sum


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} input_file")
        exit(1)

    lines = []
    with open(sys.argv[1], "r") as f:
        lines = f.readlines()

    print(calculate_sort(lines))
