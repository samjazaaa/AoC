import sys
import re
from functools import reduce
from operator import mul


def calculate_conditional(lines):
    cleared_lines = []

    for line in lines:
        cleared_lines.append(line.replace("\n", ""))

    mul_sum = 0
    full_command = ""

    for line in cleared_lines:
        full_command += line

    matches = re.findall(r"mul\([0-9]+,[0-9]+\)|do\(\)|don't\(\)", full_command)

    while "don't()" in matches:
        pos = matches.index("don't()")
        next_do = -1
        try:
            next_do = matches.index("do()", pos)
        except ValueError:
            pass
        if next_do == -1:
            del matches[pos:]
            break
        else:
            # remove between pos and next do
            del matches[pos : next_do + 1]

    # remove stray dos
    matches = list(filter(lambda exp: exp != "do()", matches))

    mul_sum = sum(
        map(
            lambda exp: reduce(
                mul, map(lambda s: int(s), exp.replace(")", "")[4:].split(","))
            ),
            matches,
        )
    )

    return mul_sum


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} input_file")
        exit(1)

    lines = []
    with open(sys.argv[1], "r") as f:
        lines = f.readlines()

    print(calculate_conditional(lines))
