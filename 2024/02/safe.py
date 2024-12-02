import sys


def is_safe(report):
    if report[0] == report[1]:
        return False

    asc = report[0] < report[1]  # true if asc, false if desc

    for i in range(1, len(report)):
        if report[i - 1] == report[i]:
            return False
        if asc and report[i - 1] > report[i]:
            return False
        if not asc and report[i - 1] < report[i]:
            return False
        if abs(report[i] - report[i - 1]) > 3:
            return False

    return True


def calculate_safe(lines):
    cleared_lines = []

    for line in lines:
        cleared_lines.append(line.replace("\n", ""))

    safe_sum = 0

    for line in cleared_lines:
        report = list(map(lambda s: int(s), line.split(" ")))
        if is_safe(report):
            safe_sum += 1

    return safe_sum


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} input_file")
        exit(1)

    lines = []
    with open(sys.argv[1], "r") as f:
        lines = f.readlines()

    print(calculate_safe(lines))
