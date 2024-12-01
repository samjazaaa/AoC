import sys


def calculate_similarity(lines):
    cleared_lines = []

    for line in lines:
        cleared_lines.append(line.replace("\n", ""))

    similarity = 0
    left = []
    right = []

    for line in cleared_lines:
        l, r = list(map(lambda val: int(val), line.split("   ")))
        left.append(l)
        right.append(r)

    for val in left:
        similarity += val * right.count(val)

    return similarity


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} input_file")
        exit(1)

    lines = []
    with open(sys.argv[1], "r") as f:
        lines = f.readlines()

    print(calculate_similarity(lines))
