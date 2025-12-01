import sys


def calculate_scores(lines):
    cleared_lines = []

    for line in lines:
        cleared_lines.append(line.replace("\n", ""))

    topo_map = [list(map(lambda v: int(v), list(line))) for line in cleared_lines]

    score_sum = 0

    for y, line in enumerate(topo_map):
        for x, height in enumerate(line):
            if height != 0:
                continue

            # TODO calculate score for current head

    return score_sum


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} input_file")
        exit(1)

    lines = []
    with open(sys.argv[1], "r") as f:
        lines = f.readlines()

    print(calculate_scores(lines))
