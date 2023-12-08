import sys


def parse_nodes(lines):
    nodes = {}

    for line in lines:
        name = line[:3]
        left, right = line[7:].replace(")", "").split(", ")
        nodes[name] = (left, right)

    return nodes


def calculate_count(lines):
    cleared_lines = []

    for line in lines:
        cleared_lines.append(line.replace("\n", ""))

    sequence = cleared_lines[0]

    nodes = parse_nodes(cleared_lines[2:])

    path_length = 0
    current_node = "AAA"
    current_seq = 0
    while current_node != "ZZZ":
        if sequence[current_seq] == "L":
            current_node = nodes[current_node][0]
        elif sequence[current_seq] == "R":
            current_node = nodes[current_node][1]
        else:
            print("invalid direction input!")
            exit(1)

        path_length += 1
        current_seq = (current_seq + 1) % len(sequence)

    return path_length


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} input_file")
        exit(1)

    lines = []
    with open(sys.argv[1], "r") as f:
        lines = f.readlines()

    print(calculate_count(lines))
