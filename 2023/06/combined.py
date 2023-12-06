import sys
from math import sqrt, ceil, floor


def calculate_combined(lines):
    cleared_lines = []

    for line in lines:
        cleared_lines.append(line.replace("\n", ""))

    time = int(cleared_lines[0].replace("Time: ", "").replace(" ", ""))
    record = int(cleared_lines[1].replace("Distance: ", "").replace(" ", ""))

    # d = v*t_2
    # v = t_1*a
    # t_1 + t_2 = t

    # d(t_1) = v*t_2 = (t_1*a)*t_2 = t_1*a*(t-t_1) = t_1*1*(t-t_1) = -t_1^2+t*t_1

    # d_r(t_1) = d(t_1) - r = -t_1^2 + t*t_1 - r > 0

    # t_a,b = (-t+-sqrt(t^2-4*-1*-r))/2*-1 = (-t+-sqrt(t^2-4r))/-2

    lower = (-time + sqrt(time**2 - 4 * record)) / (-2.0)
    upper = (-time - sqrt(time**2 - 4 * record)) / (-2.0)
    lower_bound = lower + 1 if lower.is_integer() else ceil(lower)
    upper_bound = upper - 1 if upper.is_integer() else floor(upper)

    count = upper_bound - lower_bound + 1

    return count


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} input_file")
        exit(1)

    lines = []
    with open(sys.argv[1], "r") as f:
        lines = f.readlines()

    print(calculate_combined(lines))
