import sys


def calculate_cross(lines):
    cleared_lines = []

    for line in lines:
        cleared_lines.append(line.replace("\n", ""))

    find_sum = 0

    y_max = len(cleared_lines) - 1
    x_max = len(cleared_lines[0]) - 1

    for y, line in enumerate(cleared_lines):
        for x, c in enumerate(line):
            if c == "A":
                if y >= 1 and y <= y_max - 1 and x >= 1 and x <= x_max - 1:
                    if (
                        (
                            cleared_lines[y - 1][x - 1] == "M"
                            and cleared_lines[y + 1][x + 1] == "S"
                        )
                        or (
                            cleared_lines[y - 1][x - 1] == "S"
                            and cleared_lines[y + 1][x + 1] == "M"
                        )
                    ) and (
                        (
                            cleared_lines[y - 1][x + 1] == "M"
                            and cleared_lines[y + 1][x - 1] == "S"
                        )
                        or (
                            cleared_lines[y - 1][x + 1] == "S"
                            and cleared_lines[y + 1][x - 1] == "M"
                        )
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

    print(calculate_cross(lines))
