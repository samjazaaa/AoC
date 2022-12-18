import sys

from itertools import cycle


def drop_rock(type, jets, blocked, highest_point):
    rock_positions = []

    # spawn: 2 space left, 3 space to highest point
    if type == "-":
        for x in range(2, 6):
            rock_positions.append((x, highest_point + 4))
    elif type == "+":
        rock_positions.append((3, highest_point + 6))
        rock_positions.append((3, highest_point + 4))
        for x in range(2, 5):
            rock_positions.append((x, highest_point + 5))
    elif type == "L":
        for x in range(2, 5):
            rock_positions.append((x, highest_point + 4))
        rock_positions.append((4, highest_point + 5))
        rock_positions.append((4, highest_point + 6))
    elif type == "I":
        for y in range(highest_point + 4, highest_point + 8):
            rock_positions.append((2, y))
    elif type == "#":
        rock_positions.append((2, highest_point + 4))
        rock_positions.append((2, highest_point + 5))
        rock_positions.append((3, highest_point + 4))
        rock_positions.append((3, highest_point + 5))

    stopped = False

    while not stopped:
        # chamber is 7 wide => [0,6] are allowed positions

        # jet move
        direction = next(jets)
        if direction == "<":
            new_positions = [
                (position[0] - 1, position[1]) for position in rock_positions
            ]
            if not any(
                map(
                    lambda pos: pos in blocked or pos[0] < 0 or pos[0] > 6,
                    new_positions,
                )
            ):
                rock_positions = new_positions

        elif direction == ">":
            new_positions = [
                (position[0] + 1, position[1]) for position in rock_positions
            ]
            if not any(
                map(
                    lambda pos: pos in blocked or pos[0] < 0 or pos[0] > 6,
                    new_positions,
                )
            ):
                rock_positions = new_positions

        # drop move
        new_positions = [
            (position[0], position[1] - 1) for position in rock_positions
        ]

        if not any(
            map(
                lambda pos: pos in blocked or pos[1] <= 0,
                new_positions,
            )
        ):
            rock_positions = new_positions
            continue

        stopped = True
        for position in rock_positions:
            blocked.add(position)

    highest_rock = max([field[1] for field in rock_positions])

    return highest_rock if highest_rock > highest_point else highest_point


def calculate_drop(lines):

    jet_line = cycle(lines[0].replace("\n", ""))
    shapes = cycle(["-", "+", "L", "I", "#"])

    highest_point = 0
    blocked = set()  # could also be list

    # drop 2022 rocks
    for _ in range(2022):
        highest_point = drop_rock(
            next(shapes), jet_line, blocked, highest_point
        )

    return highest_point


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} input_file")
        exit(1)

    lines = []
    with open(sys.argv[1], "r") as f:
        lines = f.readlines()

    print(calculate_drop(lines))
