#! /usr/bin/env python3

import sys


def parse_connection(line):

    points = [tuple(int(val) for val in point.split(','))
              for point in line.split(' -> ')]

    return points


def get_intersections(file_name) -> int:
    lines = []
    with open(file_name, 'r') as f:
        lines = [line.rstrip() for line in f.readlines()]

    connections = [parse_connection(line) for line in lines]

    # initialize 1kx1k grid
    grid = [[0 for _ in range(1000)] for _ in range(1000)]

    # insert all connections into grid
    for connection in connections:
        if connection[0][0] == connection[1][0]:
            # vertical line
            x = connection[0][0]
            start = connection[0][1]
            end = connection[1][1]
            sequence = range(
                start, end+1) if start < end else range(start, end-1, -1)
            for y in sequence:
                grid[y][x] += 1
        elif connection[0][1] == connection[1][1]:
            # horizontal line
            y = connection[0][1]
            start = connection[0][0]
            end = connection[1][0]
            sequence = range(
                start, end+1) if start < end else range(start, end-1, -1)
            for x in sequence:
                grid[y][x] += 1
        else:
            # diagonal => only for part 2
            continue

    # count cells with val >= 2
    return len(list(filter(lambda x: x > 1, sum(grid, []))))


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: %s <input_file>' % sys.argv[0])
        exit(1)

    print(get_intersections(sys.argv[1]))
