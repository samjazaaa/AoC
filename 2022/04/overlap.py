import sys

def line_overlap(line):
    first, second = line.replace('\n','').split(',')
    first_limits = [int(limit) for limit in first.split('-')]
    second_limits = [int(limit) for limit in second.split('-')]
    
    # first before second
    if first_limits[1] < second_limits[0]:
        return 0

    # second before first
    if second_limits[1] < first_limits[0]:
        return 0

    return 1


def calculate_overlap(lines):
    contains = 0

    for line in lines:
        contains += line_overlap(line)

    return contains


if (__name__ == '__main__'):
    if (len(sys.argv) != 2):
        print(f'Usage: {sys.argv[0]} input_file')
        exit(1)

    lines = []
    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()

    print(calculate_overlap(lines))
