import sys


def parse_values(lines):
    values = []

    for line in lines:
        value_list = [int(val) for val in line.split(" ")]
        values.append(value_list)

    return values


def extrapolate(value_list):
    if all(map(lambda val: val == 0, value_list)):
        return 0

    levels = []
    levels.append(value_list)

    current_diffs = value_list
    while not all(map(lambda val: val == 0, current_diffs)):
        new_diffs = [
            current_diffs[i] - current_diffs[i - 1]
            for i in range(1, len(current_diffs))
        ]
        levels.append(new_diffs)
        current_diffs = new_diffs

    for i in range(len(levels) - 1, 0, -1):
        ref = levels[i]
        lower = levels[i - 1]
        lower.insert(0, lower[0] - ref[0])

    return levels[0][0]


def calculate_backwards(lines):
    cleared_lines = []

    for line in lines:
        cleared_lines.append(line.replace("\n", ""))

    values = parse_values(cleared_lines)

    sum = 0
    for value_list in values:
        sum += extrapolate(value_list)

    return sum


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} input_file")
        exit(1)

    lines = []
    with open(sys.argv[1], "r") as f:
        lines = f.readlines()

    print(calculate_backwards(lines))
