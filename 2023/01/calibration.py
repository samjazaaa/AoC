import sys


def extract_value(line):
    first_digit = "0"
    second_digit = "0"

    for c in line:
        if ord(c) in range(ord("0"), ord("9") + 1):
            first_digit = c
            break

    for c in line[::-1]:
        if ord(c) in range(ord("0"), ord("9") + 1):
            second_digit = c
            break

    return int(first_digit + second_digit)


def calculate_calibration(lines):
    cleared_lines = []

    for line in lines:
        cleared_lines.append(line.replace("\n", ""))

    calibration_sum = 0

    for line in cleared_lines:
        calibration_sum += extract_value(line)

    return calibration_sum


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} input_file")
        exit(1)

    lines = []
    with open(sys.argv[1], "r") as f:
        lines = f.readlines()

    print(calculate_calibration(lines))
