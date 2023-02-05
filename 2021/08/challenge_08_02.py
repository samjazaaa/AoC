#! /usr/bin/env python3

import sys


segments_numbers = {
    'abcefg': 0,
    'cf': 1,
    'acdeg': 2,
    'acdfg': 3,
    'bcdf': 4,
    'abdfg': 5,
    'abdefg': 6,
    'acf': 7,
    'abcdefg': 8,
    'abcdfg': 9,
}


def parse_patterns(lines):

    patterns = [line.split(' | ')[0].split(' ') for line in lines]
    outputs = [line.split(' | ')[1].split(' ') for line in lines]

    return (patterns, outputs)


def analyze(pattern, output) -> int:

    # key: wire (randomized), value: segment id according to num_seg
    wire_to_segment = {
        'a': '',
        'b': '',
        'c': '',
        'd': '',
        'e': '',
        'f': '',
        'g': '',
    }

    # find unique lengths
    one = []
    four = []
    seven = []
    for val in pattern:
        if len(val) == 2:
            one = val
        elif len(val) == 4:
            four = val
        elif len(val) == 3:
            seven = val

    # find segment a (additional wire in 3 compared to 2)
    for wire in seven:
        if wire not in one:
            wire_to_segment[wire] = 'a'

    # 9 time f + 8 times c
    sum = 0
    target = one[0]
    for val in pattern:
        if target in val:
            sum += 1
    if sum == 8:  # target was segment c
        wire_to_segment[target] = 'c'
        wire_to_segment[one[1]] = 'f'
    elif sum == 9:  # target was segment f
        wire_to_segment[target] = 'f'
        wire_to_segment[one[1]] = 'c'
    else:
        print('error: %d' % sum)
        return -1

    # number 4 contains b (6x) and d (7x) in addition to already known c and f
    b_and_d = four.replace(one[0], '').replace(one[1], '')
    sum = 0
    target = b_and_d[0]
    for val in pattern:
        if target in val:
            sum += 1
    if sum == 6:  # target was segment b
        wire_to_segment[target] = 'b'
        wire_to_segment[b_and_d[1]] = 'd'
    elif sum == 7:  # target was segment d
        wire_to_segment[target] = 'd'
        wire_to_segment[b_and_d[1]] = 'b'
    else:
        print('error: %d' % sum)
        return -1

    # remaining e 4 and g 7
    remaining = ''
    for wire, segment in wire_to_segment.items():
        if segment == '':
            remaining += wire

    sum = 0
    target = remaining[0]
    for val in pattern:
        if target in val:
            sum += 1
    if sum == 4:  # target was segment e
        wire_to_segment[target] = 'e'
        wire_to_segment[remaining[1]] = 'g'
    elif sum == 7:  # target was segment g
        wire_to_segment[target] = 'g'
        wire_to_segment[remaining[1]] = 'e'
    else:
        print('error: %d' % sum)
        return -1

    output_string = ''
    for digit in output:
        translated = "".join(
            sorted("".join([wire_to_segment[wire] for wire in digit])))
        output_string += str(segments_numbers[translated])

    return int(output_string)


def get_digits(file_name) -> int:
    lines = []
    with open(file_name, 'r') as f:
        lines = [line.rstrip() for line in f.readlines()]

    patterns, outputs = parse_patterns(lines)

    sum = 0
    for pattern, output in zip(patterns, outputs):
        sum += analyze(pattern, output)

    return sum


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: %s <input_file>' % sys.argv[0])
        exit(1)

    print(get_digits(sys.argv[1]))
