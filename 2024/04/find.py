import sys


def calculate_find(lines):
    cleared_lines = []

    for line in lines:
        cleared_lines.append(line.replace("\n", ""))

    find_sum = 0

    y_max = len(cleared_lines) - 1
    x_max = len(cleared_lines[0]) - 1

    for y, line in enumerate(cleared_lines):
        for x, c in enumerate(line):
            if c == "X":
                # horizontal
                if x <= x_max - 3:
                    if (
                        cleared_lines[y][x + 1] == "M"
                        and cleared_lines[y][x + 2] == "A"
                        and cleared_lines[y][x + 3] == "S"
                    ):
                        find_sum += 1
                if x >= 3:
                    if (
                        cleared_lines[y][x - 1] == "M"
                        and cleared_lines[y][x - 2] == "A"
                        and cleared_lines[y][x - 3] == "S"
                    ):
                        find_sum += 1
                # vertical
                if y <= y_max - 3:
                    if (
                        cleared_lines[y + 1][x] == "M"
                        and cleared_lines[y + 2][x] == "A"
                        and cleared_lines[y + 3][x] == "S"
                    ):
                        find_sum += 1
                if y >= 3:
                    if (
                        cleared_lines[y - 1][x] == "M"
                        and cleared_lines[y - 2][x] == "A"
                        and cleared_lines[y - 3][x] == "S"
                    ):
                        find_sum += 1
                # diagonal
                if x <= x_max - 3 and y <= y_max - 3:
                    if (
                        cleared_lines[y + 1][x + 1] == "M"
                        and cleared_lines[y + 2][x + 2] == "A"
                        and cleared_lines[y + 3][x + 3] == "S"
                    ):
                        find_sum += 1
                if x >= 3 and y <= y_max - 3:
                    if (
                        cleared_lines[y + 1][x - 1] == "M"
                        and cleared_lines[y + 2][x - 2] == "A"
                        and cleared_lines[y + 3][x - 3] == "S"
                    ):
                        find_sum += 1
                if x >= 3 and y >= 3:
                    if (
                        cleared_lines[y - 1][x - 1] == "M"
                        and cleared_lines[y - 2][x - 2] == "A"
                        and cleared_lines[y - 3][x - 3] == "S"
                    ):
                        find_sum += 1
                if x <= x_max - 3 and y >= 3:
                    if (
                        cleared_lines[y - 1][x + 1] == "M"
                        and cleared_lines[y - 2][x + 2] == "A"
                        and cleared_lines[y - 3][x + 3] == "S"
                    ):
                        find_sum += 1
    return find_sum


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} input_file")
        exit(1)

    lines = []
    with open(sys.argv[1], "r") as f:
        lines = f.readlines()

    print(calculate_find(lines))
