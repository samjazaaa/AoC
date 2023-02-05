#! /usr/bin/env python3

import sys
import re


def parse_input_lines(lines):

    draws = [int(x) for x in lines[0].split(',')]

    board_lines = lines[1:]
    board_chunks = [board_lines[x+1:x+6]
                    for x in range(0, len(board_lines), 6)]

    boards = map(lambda chunk: list(map(lambda line: list(map(
        lambda num: int(num), re.sub(' +', ' ', line).split(' '))), chunk)),
        board_chunks)

    return (draws, list(boards))


def get_winner(file_name) -> int:
    lines = []
    with open(file_name, 'r') as f:
        lines = [line.strip() for line in f.readlines()]

    draws, boards = parse_input_lines(lines)
    transposed_boards = [list(zip(*board)) for board in boards]

    for draw in draws:
        # mark hits as -1
        for board in boards + transposed_boards:
            for line in board:
                if draw in line:
                    index = line.index(draw)
                    line[index] = -1

        for board in boards + transposed_boards:
            for line in board:
                if all(map(lambda c: True if c == -1 else False, line)):
                    # calc val and return
                    return draw * sum(filter(lambda x: x != -1,
                                             sum(board, [])))

    return -1


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: %s <input_file>' % sys.argv[0])
        exit(1)

    print(get_winner(sys.argv[1]))
