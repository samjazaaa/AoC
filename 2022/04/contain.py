import sys

def line_contains(line):
    first, second = line.replace('\n','').split(',')
    first_limits = [int(limit) for limit in first.split('-')]
    second_limits = [int(limit) for limit in second.split('-')]
    
    # first in second
    if first_limits[0] >= second_limits[0] and first_limits[1] <= second_limits[1]:
        return 1

    # second in first
    if second_limits[0] >= first_limits[0] and second_limits[1] <= first_limits[1]:
        return 1

    return 0


def calculate_contains(lines):
    contains = 0

    for line in lines:
        contains += line_contains(line)

    return contains


if (__name__ == '__main__'):
    if (len(sys.argv) != 2):
        print(f'Usage: {sys.argv[0]} input_file')
        exit(1)

    lines = []
    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()

    print(calculate_contains(lines))
