import sys

from itertools import combinations


def parse_cubes(lines):
    cubes = []

    for line in lines:
        cubes.append(
            tuple(map(lambda val: int(val), line.replace("\n", "").split(",")))
        )

    return cubes


def adjacent(cube_a, cube_b):
    return (
        abs(cube_a[0] - cube_b[0])
        + abs(cube_a[1] - cube_b[1])
        + abs(cube_a[2] - cube_b[2])
        == 1
    )


def calculate_surface(lines):

    cubes = parse_cubes(lines)

    surface = len(cubes) * 6
    for cube_a, cube_b in combinations(cubes, 2):
        # print(f"check {cube_a} and {cube_b}")
        if not adjacent(cube_a, cube_b):
            continue

        # print("adjacent!")
        surface -= 2

    return surface


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} input_file")
        exit(1)

    lines = []
    with open(sys.argv[1], "r") as f:
        lines = f.readlines()

    print(calculate_surface(lines))
