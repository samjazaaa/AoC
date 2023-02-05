import sys

def group_priority(group_lines):
    for l in group_lines[0]:
        if l in group_lines[1] and l in group_lines[2]:
            return (ord(l)-96) if (ord(l)-96) > 0 else (ord(l)-38)
    return -1


def calculate_group(lines):
    priority = 0

    for i in range(0,len(lines),3):
        priority += group_priority(lines[i:i+3])

    return priority


if (__name__ == '__main__'):
    if (len(sys.argv) != 2):
        print(f'Usage: {sys.argv[0]} input_file')
        exit(1)

    lines = []
    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()

    print(calculate_group(lines))
