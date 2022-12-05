import sys


def parse_moves(move_lines):
    moves = []
    for line in move_lines:
        count_string, rest = line.replace('move ', '').split(' from ')
        count = int(count_string)
        src, dest = [int(stack) for stack in rest.split(' to ')]
        moves.append((count, src, dest))

    return moves


def parse_stacks(stack_lines):
    stack_count = len(stack_lines[-1].split('   '))
    stacks = []

    for i in range(stack_count):
        stacks.append([])
        for line in stack_lines[-2::-1]:
            val = line[(i*4)+1]
            if val == ' ':
                break
            stacks[i].append(val)

    return stacks


def apply_moves(stacks, moves):

    for move in moves:
        elements = stacks[move[1]-1][-move[0]:]
        stacks[move[1]-1] = stacks[move[1]-1][:-move[0]]
        stacks[move[2]-1].extend(elements)


def top_vals(stacks):
    vals = ''
    for stack in stacks:
        if len(stack) > 0:
            vals += stack.pop()
    return vals


def calculate_multi_tops(lines):
    separator = lines.index('\n')

    stacks = parse_stacks(lines[:separator])
    moves = parse_moves(lines[separator+1:])

    apply_moves(stacks, moves)

    return top_vals(stacks)


if (__name__ == '__main__'):
    if (len(sys.argv) != 2):
        print(f'Usage: {sys.argv[0]} input_file')
        exit(1)

    lines = []
    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()

    print(calculate_multi_tops(lines))
