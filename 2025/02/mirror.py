import sys


def calculate_mirrors(lines):
    cleared_lines = []

    for line in lines:
        cleared_lines.append(line.replace("\n", ""))

    mirror_sum = 0

    ranges = list(map(lambda r: r.split("-"), cleared_lines[0].split(",")))

    for r in ranges:
        for val in range(int(r[0]), int(r[1]) + 1):
            str_val = str(val)
            str_len = len(str_val)
            if str_len % 2 == 1:
                continue
            if str_val[0 : (str_len // 2)] == str_val[(str_len // 2) :]:
                mirror_sum += val

    return mirror_sum


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} input_file")
        exit(1)

    lines = []
    with open(sys.argv[1], "r") as f:
        lines = f.readlines()

    print(calculate_mirrors(lines))
