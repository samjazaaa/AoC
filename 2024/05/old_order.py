import sys
import math


def is_ordered(seq, order):
    highest = -1
    for val in seq:
        if not val in order:
            continue

        if val in order and highest != -1 and order.index(val) < highest:
            return False

        highest = order.index(val)

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

    # order all rules
    numbers = set()
    for pair in rules:
        numbers.add(pair[0])
        numbers.add(pair[1])

    order = []
    for _ in range(len(numbers)):
        current_lowest = numbers.pop()
        numbers.add(current_lowest)
        for rule in rules:
            if rule[1] == current_lowest and rule[0] in numbers:
                current_lowest = rule[0]

        order.append(current_lowest)
        numbers.remove(current_lowest)

    print(order)

    middle_sum = 0

    # this does not work because: x < y | y < z  => z, x still okay (no transitive order)
    # apply order to sequences
    for seq in sequences:
        if is_ordered(seq, order):
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
