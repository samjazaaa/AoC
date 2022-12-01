import sys


def max_calories(lines):
    sums = [0]

    for line in lines:
        if line == '\n':
            sums.append(0)
            continue
        sums[-1] += int(line)

    return max(sums)


if (__name__ == '__main__'):
    if (len(sys.argv) != 2):
        print(f'Usage: {sys.argv[0]} input_file')
        exit(1)

    lines = []
    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()

    print(max_calories(lines))
