import sys


def parse_moves(lines):
    moves = []

    for line in lines:
        direction, count = line.replace('\n', '').split(' ')
        for _ in range(int(count)):
            moves.append(direction)

    return moves


def move_head(head, dir):
    if dir == 'L':
        head[0] = head[0] - 1
    if dir == 'R':
        head[0] = head[0] + 1
    if dir == 'U':
        head[1] = head[1] + 1
    if dir == 'D':
        head[1] = head[1] - 1

    return head


def adjust_tail(head, tail):
    delta_x = head[0] - tail[0]
    delta_y = head[1] - tail[1]

    # tail does not move if stacked or directly / diagonally adjacent
    if abs(delta_x) < 2 and abs(delta_y) < 2:
        return

    # new diagonal case
    if abs(delta_x) == 2 and abs(delta_y) == 2:
        tail[0] = head[0] - int((delta_x / 2))
        tail[1] = head[1] - int((delta_y / 2))
        return

    # horizontal cases
    if delta_x == 2:
        # move right
        tail[0] = head[0] - 1  # place tail right behind head
        tail[1] = head[1]  # no change if move was straight
        return
    if delta_x == -2:
        # move left
        tail[0] = head[0] + 1
        tail[1] = head[1]  # no change if move was straight
        return

    # vertical cases
    if delta_y == 2:
        # move up
        tail[1] = head[1] - 1
        tail[0] = head[0]  # no change if move was straight
        return
    if delta_y == -2:
        # move down
        tail[1] = head[1] + 1
        tail[0] = head[0]  # no change if move was straight
        return


# used for debugging
def print_rope(rope):
    for index, knot in enumerate(rope):
        print(f"{index}: {knot}")
    print('----')


def calculate_long(lines):

    moves = parse_moves(lines)

    rope = [[0, 0] for _ in range(10)]
    visited = set()
    visited.add((rope[9][0], rope[9][1]))  # starting point is already visited

    for move in moves:
        rope[0] = move_head(rope[0], move)
        for i in range(9):
            adjust_tail(rope[i], rope[i+1])
        visited.add((rope[9][0], rope[9][1]))

    return len(visited)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} input_file")
        exit(1)

    lines = []
    with open(sys.argv[1], "r") as f:
        lines = f.readlines()

    print(calculate_long(lines))
