import sys


def parse_cave(lines):
    cave = {}

    for line in lines:
        points = list(
            map(
                lambda point: tuple(
                    map(lambda val: int(val), point.split(","))
                ),
                line.replace("\n", "").split(" -> "),
            )
        )

        starting_point = points[0]
        cave[(starting_point[0], starting_point[1])] = "#"

        # add connections for remaing points if exist
        for i in range(1, len(points)):
            new_point = points[i]
            prev_point = points[i - 1]

            # vertical lines
            if new_point[0] == prev_point[0]:
                direction = 1 if new_point[1] < prev_point[1] else -1
                for y in range(new_point[1], prev_point[1], direction):
                    cave[(new_point[0], y)] = "#"
                continue

            # horizontal lines
            if new_point[1] == prev_point[1]:
                direction = 1 if new_point[0] < prev_point[0] else -1
                for x in range(new_point[0], prev_point[0], direction):
                    cave[(x, new_point[1])] = "#"
                continue

    return cave


def drop_sand(cave, max_y):
    sand_pos = [500, 0]
    while sand_pos[1] < max_y:

        # check directly below
        if (sand_pos[0], sand_pos[1]+1) not in cave:
            sand_pos[1] = sand_pos[1] + 1
            continue

        # check diagonal left
        if (sand_pos[0]-1, sand_pos[1]+1) not in cave:
            sand_pos[0] = sand_pos[0] - 1
            sand_pos[1] = sand_pos[1] + 1
            continue

        # check diagonal right
        if (sand_pos[0]+1, sand_pos[1]+1) not in cave:
            sand_pos[0] = sand_pos[0] + 1
            sand_pos[1] = sand_pos[1] + 1
            continue

        # nowhere to drop
        cave[tuple(sand_pos)] = 'o'
        return True

    return False


def calculate_rest(lines):

    cave = parse_cave(lines)
    # calc lowest y of stone => if sand is lower it drops
    max_y = 0
    for stone in cave.keys():
        if stone[1] > max_y:
            max_y = stone[1]

    resting = 0

    while drop_sand(cave, max_y):
        resting += 1

    return resting


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} input_file")
        exit(1)

    lines = []
    with open(sys.argv[1], "r") as f:
        lines = f.readlines()

    print(calculate_rest(lines))
