import sys


def parse_numbers(lines):
    numbers = []

    for y, line in enumerate(lines):
        tmp_str = ""
        tmp_coords = []
        for x, c in enumerate(line):
            if ord(c) in range(ord("0"), ord("9") + 1):
                tmp_str += c
                tmp_coords.append((x, y))
                continue

            if len(tmp_coords) > 0:
                numbers.append({"number": int(tmp_str), "coords": tmp_coords})
                tmp_str = ""
                tmp_coords = []

        if len(tmp_coords) > 0:
            numbers.append({"number": int(tmp_str), "coords": tmp_coords})
            tmp_str = ""
            tmp_coords = []

    return numbers


def is_symbol(x, y, lines):
    height = len(lines)
    width = len(lines[0])

    if x < 0 or x >= width or y < 0 or y >= height:
        return False

    val = lines[y][x]

    if not (ord(val) in range(ord("0"), ord("9") + 1) or val == "."):
        return True

    return False


def calculate_parts(lines):
    cleared_lines = []

    for line in lines:
        cleared_lines.append(line.replace("\n", ""))

    part_sum = 0

    numbers = parse_numbers(cleared_lines)

    for number in numbers:
        for x, y in number["coords"]:
            if (
                is_symbol(x - 1, y, cleared_lines)
                or is_symbol(x + 1, y, cleared_lines)
                or is_symbol(x, y - 1, cleared_lines)
                or is_symbol(x, y + 1, cleared_lines)
                or is_symbol(x - 1, y - 1, cleared_lines)
                or is_symbol(x + 1, y - 1, cleared_lines)
                or is_symbol(x - 1, y + 1, cleared_lines)
                or is_symbol(x + 1, y + 1, cleared_lines)
            ):
                part_sum += number["number"]
                break

    return part_sum


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} input_file")
        exit(1)

    lines = []
    with open(sys.argv[1], "r") as f:
        lines = f.readlines()

    print(calculate_parts(lines))
