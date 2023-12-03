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


def is_adjacent(number, x, y):
    return any(
        map(
            lambda coord: abs(coord[0] - x) <= 1 and abs(coord[1] - y) <= 1,
            number["coords"],
        )
    )


def calculate_ratios(lines):
    cleared_lines = []

    for line in lines:
        cleared_lines.append(line.replace("\n", ""))

    ratio_sum = 0

    numbers = parse_numbers(cleared_lines)

    for y, line in enumerate(cleared_lines):
        for x, c in enumerate(line):
            if c == "*":
                adjacent_numbers = list(
                    filter(lambda num: is_adjacent(num, x, y), numbers)
                )

                if len(adjacent_numbers) == 2:
                    ratio_sum += (
                        adjacent_numbers[0]["number"] * adjacent_numbers[1]["number"]
                    )

    return ratio_sum


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} input_file")
        exit(1)

    lines = []
    with open(sys.argv[1], "r") as f:
        lines = f.readlines()

    print(calculate_ratios(lines))
