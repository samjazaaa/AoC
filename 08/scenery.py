import sys


def calculate_scenery(lines):

    cleared_lines = []

    for line in lines:
        cleared_lines.append(line.replace('\n', ''))

    max_x = len(cleared_lines[0])-1
    max_y = len(cleared_lines)-1

    best_scenery = 0

    for y in range(max_y+1):
        for x in range(max_x+1):

            # edge trees always have scenery 0
            if y == 0 or y == max_y:
                continue
            if x == 0 or x == max_x:
                continue

            own_height = cleared_lines[y][x]

            # check left
            left_scenery = 0
            for x_new in range(x-1, -1, -1):
                left_scenery += 1
                if cleared_lines[y][x_new] >= own_height:
                    break

            # check right
            right_scenery = 0
            for x_new in range(x+1, max_x+1):
                right_scenery += 1
                if cleared_lines[y][x_new] >= own_height:
                    break

            # check top
            top_scenery = 0
            for y_new in range(y-1, -1, -1):
                top_scenery += 1
                if cleared_lines[y_new][x] >= own_height:
                    break

            # check bottom
            bot_scenery = 0
            for y_new in range(y+1, max_y+1):
                bot_scenery += 1
                if cleared_lines[y_new][x] >= own_height:
                    break

            scenery = left_scenery * right_scenery * top_scenery * bot_scenery

            if scenery > best_scenery:
                best_scenery = scenery

    return best_scenery


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} input_file")
        exit(1)

    lines = []
    with open(sys.argv[1], "r") as f:
        lines = f.readlines()

    print(calculate_scenery(lines))
