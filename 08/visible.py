import sys


def calculate_visible(lines):

    cleared_lines = []

    for line in lines:
        cleared_lines.append(line.replace('\n', ''))

    max_x = len(cleared_lines[0])-1
    max_y = len(cleared_lines)-1

    visible = 0

    for y in range(max_y+1):
        for x in range(max_x+1):

            if y == 0 or y == max_y:
                visible += 1
                continue
            if x == 0 or x == max_x:
                visible += 1
                continue

            own_height = cleared_lines[y][x]

            # check left
            self_visible = True
            for x_new in range(x-1, -1, -1):
                if cleared_lines[y][x_new] >= own_height:
                    self_visible = False
                    break
            if self_visible:
                visible += 1
                continue

            # check right
            self_visible = True
            for x_new in range(x+1, max_x+1):
                if cleared_lines[y][x_new] >= own_height:
                    self_visible = False
                    break
            if self_visible:
                visible += 1
                continue

            # check top
            self_visible = True
            for y_new in range(y-1, -1, -1):
                if cleared_lines[y_new][x] >= own_height:
                    self_visible = False
                    break
            if self_visible:
                visible += 1
                continue

            # check bottom
            self_visible = True
            for y_new in range(y+1, max_y+1):
                if cleared_lines[y_new][x] >= own_height:
                    self_visible = False
                    break
            if self_visible:
                visible += 1
                continue

    return visible


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} input_file")
        exit(1)

    lines = []
    with open(sys.argv[1], "r") as f:
        lines = f.readlines()

    print(calculate_visible(lines))
