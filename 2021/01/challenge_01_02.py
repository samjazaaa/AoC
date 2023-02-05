#! /usr/bin/env python3

import sys


def get_depths(file_name) -> int:

    lines = []
    with open(file_name, 'r') as f:
        lines = [int(line.rstrip()) for line in f.readlines()]

    window_sums = list(map(lambda t: t[0] + t[1] + t[2],
                           zip(lines, lines[1:], lines[2:])))

    diffs = map(lambda i, l: ((i, True)
                if (window_sums[i] > window_sums[i-1]) else (i, False))
                if i > 0 else (i, None), range(len(window_sums)), window_sums)

    incs = len(list(filter(lambda t: t[1], diffs)))

    return incs


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: %s <input_file>' % sys.argv[0])
        exit(1)

    print(get_depths(sys.argv[1]))
