import sys


def check_section(section):
    for c in section:
        if section.count(c) > 1:
            return False

    return True


def calculate_message(lines):
    line = lines[0]
    for i in range(14, len(line)):
        if check_section(line[i-14:i]):
            return i

    return -1


if (__name__ == '__main__'):
    if (len(sys.argv) != 2):
        print(f'Usage: {sys.argv[0]} input_file')
        exit(1)

    lines = []
    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()

    print(calculate_message(lines))
