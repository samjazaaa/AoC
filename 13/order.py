import sys
from itertools import zip_longest


def parse_list(line):
    parsed = []
    content = line[1:]

    i = 0  # index
    processed = 1  # how many chars have been processed in this call
    temp_val = ''  # for storing partly parsed numbers

    while i < len(content):
        if content[i] == ']':
            processed += 1
            # finish pending number processing
            if temp_val != '':
                parsed.append(int(temp_val))
                temp_val = ''
            return parsed, processed

        if content[i] == '[':
            sub_list, sub_processed = parse_list(content[i:])
            parsed.append(sub_list)
            processed += sub_processed
            i += sub_processed
            continue

        if content[i] == ',':
            processed += 1
            # finish pending number processing
            if temp_val != '':
                parsed.append(int(temp_val))
                temp_val = ''
            i += 1
            continue

        # content is a digit (or malformed input)
        temp_val += content[i]
        processed += 1
        i += 1

    print('Reached end of line while still expecting closing bracket!')
    return parsed, processed


def parse_pairs(lines):
    pairs = []

    for i in range(0, len(lines)-1, 3):
        left = parse_list(lines[i].replace('\n', ''))[0]
        right = parse_list(lines[i+1].replace('\n', ''))[0]
        pairs.append((left, right))

    return pairs


# returns 1 if right order, -1 if wrong order and 0 if identical
def check_order(pair):

    for left, right in zip_longest(pair[0], pair[1]):

        if left is None:
            return 1

        if right is None:
            return -1

        # check if both are numbers
        if not (isinstance(left, list) or isinstance(right, list)):
            if left < right:
                return 1
            elif left > right:
                return -1
            continue

        # at least one halft is list => convert both sides to list
        sub_left = left
        sub_right = right
        if not isinstance(left, list):
            sub_left = [left]
        if not isinstance(right, list):
            sub_right = [right]

        # check sub lists
        sub = check_order((sub_left, sub_right))
        if sub != 0:
            return sub

    return 0


def calculate_order(lines):

    pairs = parse_pairs(lines)

    right = 0

    for i, pair in enumerate(pairs):
        if check_order(pair) == 1:
            right += (i+1)

    return right


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} input_file")
        exit(1)

    lines = []
    with open(sys.argv[1], "r") as f:
        lines = f.readlines()

    print(calculate_order(lines))
