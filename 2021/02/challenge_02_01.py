#! /usr/bin/env python3

import sys


def get_target(file_name) -> int:
    lines = []
    with open(file_name, 'r') as f:
        lines = [line.rstrip() for line in f.readlines()]

    x = 0
    depth = 0

    for line in lines:
        dir, val = line.split(' ')
        if dir == 'forward':
            x += int(val)
        elif dir == 'down':
            depth += int(val)
        elif dir == 'up':
            depth -= int(val)
        else:
            print('unknown direction: %s' % dir)
            return 0

    return x*depth


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: %s <input_file>' % sys.argv[0])
        exit(1)

    print(get_target(sys.argv[1]))
