#! /usr/bin/env python3

import sys


def get_power(file_name) -> int:
    lines = []
    with open(file_name, 'r') as f:
        lines = [line.rstrip() for line in f.readlines()]

    columns = len(lines[0])
    col_sums = []
    for _ in range(columns):
        col_sums.append(0)

    for line in lines:
        for i, c in enumerate(line):
            col_sums[i] += int(c)

    gamma = ''
    epsilon = ''
    for i, s in enumerate(col_sums):
        if s > len(lines)/2:
            gamma += '1'
            epsilon += '0'
        elif s < len(lines)/2:
            gamma += '0'
            epsilon += '1'
        else:
            print('Both bit vals are equally common in column %d' % i)
            return 0

    return int(gamma, base=2) * int(epsilon, base=2)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: %s <input_file>' % sys.argv[0])
        exit(1)

    print(get_power(sys.argv[1]))
