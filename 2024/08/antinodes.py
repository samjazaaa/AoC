import sys
from collections import defaultdict
from itertools import combinations


def parse_antennas(lines):
    antennas = defaultdict(list)

    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == ".":
                continue

            antennas[c].append((x, y))

    return antennas


def sub_vecs(a, b):
    return (a[0] - b[0], a[1] - b[1])


def add_vecs(a, b):
    return (a[0] + b[0], a[1] + b[1])


def insert_antinodes(positions, grid):
    max_y = len(grid) - 1
    max_x = len(grid[0]) - 1

    # for all pairs of positions
    for a, b in combinations(positions, 2):
        diff = sub_vecs(b, a)

        pos1 = add_vecs(b, diff)
        pos2 = sub_vecs(a, diff)

        for vec in [pos1, pos2]:
            if vec[0] >= 0 and vec[0] <= max_x and vec[1] >= 0 and vec[1] <= max_y:
                grid[vec[1]][vec[0]] = "#"


def calculate_antinodes(lines):
    cleared_lines = []

    for line in lines:
        cleared_lines.append(line.replace("\n", ""))

    antennas = parse_antennas(cleared_lines)
    antinode_grid = [
        ["." for _ in range(len(cleared_lines[0]))] for _ in range(len(cleared_lines))
    ]

    for positions in antennas.values():
        insert_antinodes(positions, antinode_grid)

    antinode_sum = 0
    for line in antinode_grid:
        for c in line:
            if c == "#":
                antinode_sum += 1

    return antinode_sum


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} input_file")
        exit(1)

    lines = []
    with open(sys.argv[1], "r") as f:
        lines = f.readlines()

    print(calculate_antinodes(lines))
