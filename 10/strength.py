import sys


def check(cycle, x):
    if cycle in range(20, 260, 40):
        return cycle * x

    return 0


def calculate_strength(lines):

    x = 1
    cycle = 0
    sum = 0

    for line in lines:
        if line.replace('\n', '') == 'noop':
            # start the cycle
            cycle += 1
            # check if its a measuring cycle
            sum += check(cycle, x)
            # do nothing
            continue

        _, val = line.replace('\n', '').split(' ')
        # start first cycle
        cycle += 1
        # check
        sum += check(cycle, x)
        # start second cycle
        cycle += 1
        # check
        sum += check(cycle, x)
        # at the end of the second cycle update the value
        x += int(val)

    return sum


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} input_file")
        exit(1)

    lines = []
    with open(sys.argv[1], "r") as f:
        lines = f.readlines()

    print(calculate_strength(lines))
