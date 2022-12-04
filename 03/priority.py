import sys

def line_priority(line):
    first = line[:int(len(line)/2)]
    second = line[int(len(line)/2):]
    for l in first:
        if l in second:
            return (ord(l)-96) if (ord(l)-96) > 0 else (ord(l)-38)
    return -1


def calculate_priority(lines):
    priority = 0

    for line in lines:
        priority += line_priority(line)

    return priority


if (__name__ == '__main__'):
    if (len(sys.argv) != 2):
        print(f'Usage: {sys.argv[0]} input_file')
        exit(1)

    lines = []
    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()

    print(calculate_priority(lines))
