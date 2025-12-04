import sys


def max_joltage(line):

    for i in range(9, 0, -1):
        first_pos = line.find(str(i))
        if first_pos == -1 or first_pos == len(line) - 1:
            continue
        for j in range(9, 0, -1):
            second_pos = line[first_pos + 1 :].find(str(j))
            if second_pos == -1:
                continue
            return int(i * 10 + j)


def calculate_joltage(lines):
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

    print(calculate_joltage(lines))
