import sys
import math


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


def calculate_order(lines):
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

    middle_sum = 0

    for seq in sequences:
        if is_ordered(seq, rules):
            middle = math.floor(len(seq) / 2)
            middle_sum += seq[middle]

    return middle_sum


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} input_file")
        exit(1)

    lines = []
    with open(sys.argv[1], "r") as f:
        lines = f.readlines()

    print(calculate_order(lines))
