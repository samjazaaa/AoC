#! /usr/bin/env python3

import sys


def gauss_diff(target, pos) -> int:

    diff = abs(target-pos)
    return 0.5*diff*(diff+1)


def get_fuel(file_name) -> int:
    input = ""
    with open(file_name, 'r') as f:
        input = f.readline().rstrip()

    positions = [int(val) for val in input.split(',')]

    positions.sort()
    max_val = positions[len(positions) - 1]
    min_fuel = -1

    for target in range(max_val):
        fuel = sum([gauss_diff(target, pos) for pos in positions])
        if min_fuel == -1 or fuel < min_fuel:
            min_fuel = fuel
        else:
            # function is convex
            break

    return min_fuel


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: %s <input_file>' % sys.argv[0])
        exit(1)

    print(get_fuel(sys.argv[1]))
