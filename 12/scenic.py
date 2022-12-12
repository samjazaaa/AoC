import sys


def find_symbols(lines, symbols):
    found = []
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c in symbols:
                found.append((x, y))

    return found


def get_height(lines, x, y):
    return (
        "a"
        if lines[y][x] == "S"
        else "z"
        if lines[y][x] == "E"
        else lines[y][x]
    )


def check_direction(lines, x, y, height, visited):
    if x not in range(0, len(lines[0])) or y not in range(0, len(lines)):
        return None

    if (x, y) in visited:
        return None

    if ord(get_height(lines, x, y)) > ord(height) + 1:
        return None

    return (x, y)


def calculate_scenic(lines):

    cleared_lines = []

    # strip new lines
    for line in lines:
        cleared_lines.append(line.replace("\n", ""))

    # find starting pos
    start_positions = find_symbols(cleared_lines, ['S', 'a'])

    # find target
    target = find_symbols(cleared_lines, ['E'])[0]

    # BFS

    # already visited positions
    visited = set()
    for start in start_positions:
        visited.add(start)

    # possible positions and step counts
    positions = [(start, 0) for start in start_positions]

    while len(positions) > 0:
        current = positions.pop(0)
        pos, steps = current
        x, y = pos
        height = get_height(cleared_lines, x, y)

        # check steppable directions
        directions = []
        directions.append(
            check_direction(cleared_lines, x, y - 1, height, visited)
        )
        directions.append(
            check_direction(cleared_lines, x, y + 1, height, visited)
        )
        directions.append(
            check_direction(cleared_lines, x - 1, y, height, visited)
        )
        directions.append(
            check_direction(cleared_lines, x + 1, y, height, visited)
        )
        for new in directions:
            if new is not None:
                if new == target:
                    return steps + 1
                visited.add(new)
                positions.append((new, steps + 1))

    print('Target not reachable')
    return -1


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} input_file")
        exit(1)

    lines = []
    with open(sys.argv[1], "r") as f:
        lines = f.readlines()

    print(calculate_scenic(lines))
