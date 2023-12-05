import sys


def parse_seeds(line):
    return list(map(lambda s: int(s), line.replace("seeds: ", "").split(" ")))


def parse_maps(lines):
    maps = []

    blocks = []
    current_block = []
    for line in lines:
        if "" == line:
            blocks.append(current_block)
            current_block = []
            continue
        current_block.append(line)

    for block in blocks:
        parsed_map = []
        for map_range in block[1:]:
            range_vals = tuple(map(lambda n: int(n), map_range.split(" ")))
            parsed_map.append(range_vals)

        maps.append(parsed_map)

    return maps


def calculate_closest(lines):
    cleared_lines = []

    for line in lines:
        cleared_lines.append(line.replace("\n", ""))

    seeds = parse_seeds(cleared_lines[0])
    maps = parse_maps(cleared_lines[2:])

    destinations = []
    for seed in seeds:
        current_val = seed
        for map_section in maps:
            for map_range in map_section:
                if current_val in range(map_range[1], map_range[1] + map_range[2]):
                    current_val = current_val - (map_range[1] - map_range[0])
                    break

        destinations.append(current_val)

    return min(destinations)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} input_file")
        exit(1)

    lines = []
    with open(sys.argv[1], "r") as f:
        lines = f.readlines()

    print(calculate_closest(lines))
