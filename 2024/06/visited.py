import sys


def is_inside(pos, max_y, max_x):
    if pos[0] < 0 or pos[1] < 0:
        return False

    if pos[0] > max_x or pos[1] > max_y:
        return False

    return True


def do_step(lines, current, orientation, max_x, max_y):
    # mark current pos with x
    lines[current[1]][current[0]] = "X"

    # check next pos
    next = None
    if orientation == "N":
        next = [current[0], current[1] - 1]
    elif orientation == "E":
        next = [current[0] + 1, current[1]]
    elif orientation == "S":
        next = [current[0], current[1] + 1]
    elif orientation == "W":
        next = [current[0] - 1, current[1]]

    if is_inside(next, max_y, max_x) and lines[next[1]][next[0]] == "#":
        if orientation == "N":
            orientation = "E"
        elif orientation == "E":
            orientation = "S"
        elif orientation == "S":
            orientation = "W"
        elif orientation == "W":
            orientation = "N"

        return current, orientation

    # if no increase pos
    return next, orientation


def walk_path(lines):
    current = None
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == "^":
                current = [x, y]

    max_y = len(lines) - 1
    max_x = len(lines[0]) - 1
    orientation = "N"

    while is_inside(current, max_y, max_x):
        current, orientation = do_step(lines, current, orientation, max_x, max_y)


def count_visited(lines):
    count = 0

    for line in lines:
        for c in line:
            if c == "X":
                count += 1

    return count


def calculate_visited(lines):
    cleared_lines = []

    for line in lines:
        cleared_lines.append(line.replace("\n", ""))

    grid = []
    for line in cleared_lines:
        grid.append(list(line))

    walk_path(grid)

    visited_sum = count_visited(grid)

    return visited_sum


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} input_file")
        exit(1)

    lines = []
    with open(sys.argv[1], "r") as f:
        lines = f.readlines()

    print(calculate_visited(lines))
