import sys

actions = {
    'X': {
        'val': 1,
        'win': 'C',
        'loose': 'B',
        'draw': 'A'
    },
    'Y': {
        'val': 2,
        'win': 'A',
        'loose': 'C',
        'draw': 'B'
    },
    'Z': {
        'val': 3,
        'win': 'B',
        'loose': 'A',
        'draw': 'C'
    },
}


def line_score(line):
    score = 0
    opponent, own = line.replace('\n', '').split(' ')
    action = actions[own]
    score += action['val']
    if (opponent == action['win']):
        return score + 6
    if (opponent == action['draw']):
        return score + 3
    if (opponent == action['loose']):
        return score


def calculate_score(lines):
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

    print(calculate_score(lines))
