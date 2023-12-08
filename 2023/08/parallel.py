import sys
from math import lcm


def parse_nodes(lines):
    nodes = {}

    for line in lines:
        name = line[:3]
        left, right = line[7:].replace(")", "").split(", ")
        nodes[name] = (left, right)

    return nodes


def calculate_parallel(lines):
    cleared_lines = []

    for line in lines:
        cleared_lines.append(line.replace("\n", ""))

    sequence = cleared_lines[0]

    nodes = parse_nodes(cleared_lines[2:])

    start_nodes = list(filter(lambda name: name.endswith("A"), nodes.keys()))
    shortest_lengths = []

    for node in start_nodes:
        path_length = 0
        current_node = node
        current_seq = 0
        while not current_node.endswith("Z"):
            if sequence[current_seq] == "L":
                current_node = nodes[current_node][0]
            elif sequence[current_seq] == "R":
                current_node = nodes[current_node][1]
            else:
                print("invalid direction input!")
                exit(1)

            path_length += 1
            current_seq = (current_seq + 1) % len(sequence)

        shortest_lengths.append(path_length)

    return lcm(*shortest_lengths)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} input_file")
        exit(1)

    lines = []
    with open(sys.argv[1], "r") as f:
        lines = f.readlines()

    print(calculate_parallel(lines))
