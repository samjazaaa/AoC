import sys


def calculate_zeroes(lines):
    cleared_lines = []

    for line in lines:
        cleared_lines.append(line.replace("\n", ""))

    zero_count = 0
    curr = 50

    for line in lines:
        move = int(line[1:])
        if line[0] == "L":
            move = -move
        curr = (curr + move) % 100
        if curr == 0:
            zero_count += 1

    return zero_count


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} input_file")
        exit(1)

    lines = []
    with open(sys.argv[1], "r") as f:
        lines = f.readlines()

    print(calculate_zeroes(lines))
