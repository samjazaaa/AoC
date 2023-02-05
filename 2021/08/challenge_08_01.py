#! /usr/bin/env python3

import sys


def parse_patterns(lines):

    patterns = [line.split(' | ')[0].split(' ') for line in lines]
    outputs = [line.split(' | ')[1].split(' ') for line in lines]

    return (patterns, outputs)


def get_digits(file_name) -> int:
    lines = []
    with open(file_name, 'r') as f:
        lines = [line.rstrip() for line in f.readlines()]

    patterns, outputs = parse_patterns(lines)

    line_numbers = {
        0: 6,
        1: 2,
        2: 5,
        3: 5,
        4: 4,
        5: 5,
        6: 6,
        7: 3,
        8: 7,
        9: 6
    }

    targets = [line_numbers[1], line_numbers[4],
               line_numbers[7], line_numbers[8]]

    return len(list(filter(lambda i: len(i) in targets, sum(outputs, []))))


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: %s <input_file>' % sys.argv[0])
        exit(1)

    print(get_digits(sys.argv[1]))
