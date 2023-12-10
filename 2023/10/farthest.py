import sys

tiles = {
    "|": {"N": "S", "S": "N"},
    "-": {"E": "W", "W": "E"},
    "L": {"N": "E", "E": "N"},
    "J": {"N": "W", "W": "N"},
    "7": {"S": "W", "W": "S"},
    "F": {"S": "E", "E": "S"},
}


def get_start_pos(lines):
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == "S":
                return (x, y)


def calculate_farthest(lines):
    cleared_lines = []

    for line in lines:
        cleared_lines.append(line.replace("\n", ""))

    height = len(cleared_lines)
    width = len(cleared_lines[0])

    start_pos = get_start_pos(cleared_lines)
    positions = []

    # east
    if start_pos[0] < (width - 1) and cleared_lines[start_pos[1]][start_pos[0] + 1] in [
        "-",
        "J",
        "7",
    ]:
        positions.append([[start_pos[0] + 1, start_pos[1]], "W"])

    # south
    if start_pos[1] < (height - 1) and cleared_lines[start_pos[1] + 1][
        start_pos[0]
    ] in [
        "|",
        "L",
        "J",
    ]:
        positions.append([[start_pos[0], start_pos[1] + 1], "N"])

    # west
    if start_pos[0] > 0 and cleared_lines[start_pos[1]][start_pos[0] - 1] in [
        "-",
        "L",
        "F",
    ]:
        positions.append([[start_pos[0] - 1, start_pos[1]], "E"])

    # north
    if start_pos[1] > 0 and cleared_lines[start_pos[1] - 1][start_pos[0]] in [
        "|",
        "7",
        "F",
    ]:
        positions.append([[start_pos[0], start_pos[1] - 1], "S"])

    steps = 0

    while not (
        positions[0][0][0] == positions[1][0][0]
        and positions[0][0][1] == positions[1][0][1]
    ):
        for position in positions:
            location, origin = position
            symbol = cleared_lines[location[1]][location[0]]
            direction = tiles[symbol][origin]
            if direction == "E":
                location[0] = location[0] + 1
                position[1] = "W"
                continue
            if direction == "S":
                location[1] = location[1] + 1
                position[1] = "N"
                continue
            if direction == "W":
                location[0] = location[0] - 1
                position[1] = "E"
                continue
            if direction == "N":
                location[1] = location[1] - 1
                position[1] = "S"
                continue

        steps += 1

    return steps + 1


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} input_file")
        exit(1)

    lines = []
    with open(sys.argv[1], "r") as f:
        lines = f.readlines()

    print(calculate_farthest(lines))
