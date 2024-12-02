import sys


def is_safe(report):
    if report[0] == report[1]:
        return (0, 1)

    asc = report[0] < report[1]  # true if asc, false if desc

    for i in range(1, len(report)):
        if report[i - 1] == report[i]:
            return (i - 1, i)
        if asc and report[i - 1] > report[i]:
            return (i - 1, i)
        if not asc and report[i - 1] < report[i]:
            return (i - 1, i)
        if abs(report[i] - report[i - 1]) > 3:
            return (i - 1, i)

    return None


def calculate_fixed(lines):
    cleared_lines = []

    for line in lines:
        cleared_lines.append(line.replace("\n", ""))

    safe_sum = 0

    for line in cleared_lines:
        report = list(map(lambda s: int(s), line.split(" ")))
        errors = is_safe(report)
        if errors == None:
            safe_sum += 1
            continue

        first = report.copy()
        del first[errors[0]]
        second = report.copy()
        del second[errors[1]]

        if is_safe(first) == None:
            safe_sum += 1
            continue

        if is_safe(second) == None:
            safe_sum += 1
            continue

        # if first number is the actual error, we use the wrong order => extra check
        if errors[0] == 1:
            third = report.copy()
            del third[0]
            if is_safe(third) == None:
                safe_sum += 1

    return safe_sum


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} input_file")
        exit(1)

    lines = []
    with open(sys.argv[1], "r") as f:
        lines = f.readlines()

    print(calculate_fixed(lines))
