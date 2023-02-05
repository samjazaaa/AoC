#! /usr/bin/env python3

import sys
import statistics


def get_fuel(file_name) -> int:
    input = ""
    with open(file_name, 'r') as f:
        input = f.readline().rstrip()

    positions = [int(val) for val in input.split(',')]

    # median minimizes sum of absolute diffs:
    # https://math.stackexchange.com/questions/113270/the-median-minimizes-the-sum-of-absolute-deviations-the-ell-1-norm
    target = statistics.median(positions)

    fuel = sum([abs(target-pos) for pos in positions])

    return fuel


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: %s <input_file>' % sys.argv[0])
        exit(1)

    print(get_fuel(sys.argv[1]))
