import sys


def parse_forwards(line, letters):
    for i, c in enumerate(line):
        if ord(c) in range(ord("0"), ord("9") + 1):
            return c
        for letter in letters.keys():
            if line[i:].find(letter) == 0:
                return letters[letter]


def parse_backwards(line, letters):
    for i in range(len(line))[::-1]:
        if ord(line[i]) in range(ord("0"), ord("9") + 1):
            return line[i]
        for letter in letters.keys():
            if line[i:].find(letter) == 0:
                return letters[letter]


def extract_value(line):
    first_digit = "0"
    second_digit = "0"
    letters = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }

    first_digit = parse_forwards(line, letters)
    second_digit = parse_backwards(line, letters)

    return int(first_digit + second_digit)


def calculate_letters(lines):
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

    print(calculate_letters(lines))
