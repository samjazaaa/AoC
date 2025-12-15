import sys


def is_accessible(lines, row, column, max_row, max_col):

    connections = 0

    # top
    if row >= 1:
        # left
        if column >= 1 and lines[row - 1][column - 1] == "@":
            connections += 1
        # middle
        if lines[row - 1][column] == "@":
            connections += 1
        # right
        if column < max_col and lines[row - 1][column + 1] == "@":
            connections += 1

    # left
    if column >= 1 and lines[row][column - 1] == "@":
        connections += 1

    # right
    if column < max_col and lines[row][column + 1] == "@":
        connections += 1

    # bottom 3
    if row < max_row:
        # left
        if column >= 1 and lines[row + 1][column - 1] == "@":
            connections += 1
        # middle
        if lines[row + 1][column] == "@":
            connections += 1
        # right
        if column < max_col and lines[row + 1][column + 1] == "@":
            connections += 1

    print(f"row {row}, column {column}: {connections} => {connections < 4}")

    return connections < 4


def calculate_access(lines):
    cleared_lines = []

    for line in lines:
        cleared_lines.append(line.replace("\n", ""))

    rows = len(cleared_lines)
    columns = len(cleared_lines[0])

    accessible = 0

    for row in range(rows):
        for column in range(columns):
            if cleared_lines[row][column] == "@" and is_accessible(
                cleared_lines, row, column, rows - 1, columns - 1
            ):
                accessible += 1

    return accessible


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} input_file")
        exit(1)

    lines = []
    with open(sys.argv[1], "r") as f:
        lines = f.readlines()

    print(calculate_access(lines))
