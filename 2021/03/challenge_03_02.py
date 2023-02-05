#! /usr/bin/env python3

import sys


def scan_lines(lines, column, dom) -> list:

    col_sum = 0
    dom_bit = '1'

    for line in lines:
        col_sum += int(line[column])

    if col_sum < len(lines)/2:
        dom_bit = '0'

    if dom:
        return list(filter(lambda l: l[column] == dom_bit, lines))
    else:
        return list(filter(lambda l: l[column] != dom_bit, lines))


def get_power(file_name) -> int:
    lines = []
    with open(file_name, 'r') as f:
        lines = [line.rstrip() for line in f.readlines()]

    columns = len(lines[0])
    oxy_lines = lines
    co2_lines = lines.copy()

    for i in range(columns):
        oxy_lines = scan_lines(oxy_lines, i, dom=True)
        if len(oxy_lines) == 1:
            break

    if len(oxy_lines) != 1:
        print('Undecidable for oxy')
        return 0

    for i in range(columns):
        co2_lines = scan_lines(co2_lines, i, dom=False)
        if len(co2_lines) == 1:
            break

    if len(oxy_lines) != 1:
        print('Undecidable for co2')
        return 0

    return int(oxy_lines[0], base=2) * int(co2_lines[0], base=2)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: %s <input_file>' % sys.argv[0])
        exit(1)

    print(get_power(sys.argv[1]))
