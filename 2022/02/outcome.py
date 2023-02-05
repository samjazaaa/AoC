import sys

actions = {
    'A': {  # rock
        'win': 2,  # paper
        'loose': 3,  # scissor
        'draw': 1  # rock
    },
    'B': {  # paper
        'win': 3,  # scissor
        'loose': 1,  # rock
        'draw': 2  # paper
    },
    'C': {  # scissor
        'win': 1,  # rock
        'loose': 2,  # paper
        'draw': 3  # scissor
    },
}


def line_score(line):
    opponent, outcome = line.replace('\n', '').split(' ')

    action = actions[opponent]
    if (outcome == 'X'):  # loose
        return action['loose']
    if (outcome == 'Y'):  # draw
        return action['draw'] + 3
    if (outcome == 'Z'):  # win
        return action['win'] + 6


def calculate_outcome(lines):
    score = 0

    for line in lines:
        score += line_score(line)
        pass

    return score


if (__name__ == '__main__'):
    if (len(sys.argv) != 2):
        print(f'Usage: {sys.argv[0]} input_file')
        exit(1)

    lines = []
    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()

    print(calculate_outcome(lines))
