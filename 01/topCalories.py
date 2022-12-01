import sys


def top_calories(lines):
    sums = [0]

    for line in lines:
        if line == '\n':
            sums.append(0)
            continue
        sums[-1] += int(line)

    sums.sort(reverse=True)
    return sum(sums[:3])


if (__name__ == '__main__'):
    if (len(sys.argv) != 2):
        print(f'Usage: {sys.argv[0]} input_file')
        exit(1)

    lines = []
    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()

    print(top_calories(lines))
