import sys
from copy import deepcopy


def print_lines(lines, obstruction=None):
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if obstruction is not None and obstruction[0] == x and obstruction[1] == y:
                print("O", end="")
            else:
                print(c, end="")

        print()


def collect_visited(lines):
    visited = []

    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c in ["-", "|", "+"]:
                visited.append((x, y))

    return visited


def already_visited(current, orientation, log):
    for p, o in log:
        if current[0] == p[0] and current[1] == p[1] and orientation == o:
            return True

    return False


def is_inside(pos, max_y, max_x):
    if pos[0] < 0 or pos[1] < 0:
        return False

    if pos[0] > max_x or pos[1] > max_y:
        return False

    return True


def do_step(lines, current, orientation, obstruction, max_x, max_y):
    # mark current pos
    if orientation == "N" or orientation == "S":
        if lines[current[1]][current[0]] == "-":
            lines[current[1]][current[0]] = "+"
        else:
            lines[current[1]][current[0]] = "|"

    if orientation == "E" or orientation == "W":
        if lines[current[1]][current[0]] == "|":
            lines[current[1]][current[0]] = "+"
        else:
            lines[current[1]][current[0]] = "-"

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

    if is_inside(next, max_y, max_x) and (
        lines[next[1]][next[0]] == "#"
        or (
            obstruction is not None
            and (next[0] == obstruction[0] and next[1] == obstruction[1])
        )
    ):
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


def is_loop(lines, obstruction=None):
    current = None
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == "^":
                if obstruction is not None and (
                    obstruction[0] == x and obstruction[1] == y
                ):
                    return False
                current = [x, y]

    max_y = len(lines) - 1
    max_x = len(lines[0]) - 1
    orientation = "N"

    log = []

    while is_inside(current, max_y, max_x):
        log.append((current, orientation))

        current, orientation = do_step(
            lines, current, orientation, obstruction, max_x, max_y
        )

        if already_visited(current, orientation, log):
            return True

    return False


def calculate_loop(lines):
    cleared_lines = []

    for line in lines:
        cleared_lines.append(line.replace("\n", ""))

    grid = []
    for line in cleared_lines:
        grid.append(list(line))

    # do part 1 to get all X locations
    ref_grid = deepcopy(grid)
    is_loop(ref_grid)
    x_locations = collect_visited(ref_grid)

    loop_count = 0

    # this is very slow but it gets the job done I guess
    for x, y in x_locations:
        obstruction = (x, y)
        current_grid = deepcopy(grid)
        if is_loop(current_grid, obstruction):
            loop_count += 1

    return loop_count


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} input_file")
        exit(1)

    lines = []
    with open(sys.argv[1], "r") as f:
        lines = f.readlines()

    print(calculate_loop(lines))
