import sys


def calculate_distances(lines):
    cleared_lines = []

    for line in lines:
        cleared_lines.append(line.replace("\n", ""))

    distance_sum = 0
    left = []
    right = []

    for line in cleared_lines:
        l, r = list(map(lambda val: int(val), line.split("   ")))
        left.append(l)
        right.append(r)

    left.sort()
    right.sort()
    for l, r in zip(left, right):
        distance_sum += abs(l - r)

    return distance_sum


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} input_file")
        exit(1)

    lines = []
    with open(sys.argv[1], "r") as f:
        lines = f.readlines()

    print(calculate_distances(lines))
