import sys


def max_joltage(line):

    current_indent = 0
    digits = ""
    for remaining_length in range(12, 0, -1):
        for digit in range(9, 0, -1):
            pos = line[current_indent:].find(str(digit))
            if pos == -1 or len(line[current_indent + pos + 1 :]) < (
                remaining_length - 1
            ):
                continue
            digits += str(digit)
            current_indent += pos + 1
            break

    return int(digits)


def calculate_friction(lines):
    cleared_lines = []

    for line in lines:
        cleared_lines.append(line.replace("\n", ""))

    joltage_sum = 0

    for line in cleared_lines:
        joltage_sum += max_joltage(line)

    return joltage_sum


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} input_file")
        exit(1)

    lines = []
    with open(sys.argv[1], "r") as f:
        lines = f.readlines()

    print(calculate_friction(lines))
