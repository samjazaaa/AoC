import sys


def parse_seeds(line):
    inputs = list(map(lambda s: int(s), line.replace("seeds: ", "").split(" ")))
    seed_ranges = [tuple(inputs[i : i + 2]) for i in range(0, len(inputs), 2)]

    return seed_ranges


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


def calculate_ranges(lines):
    cleared_lines = []

    for line in lines:
        cleared_lines.append(line.replace("\n", ""))

    seed_ranges = parse_seeds(cleared_lines[0])

    maps = parse_maps(cleared_lines[2:])

    destinations = []
    for seed_range in seed_ranges:
        range_start, range_length, current_skip = (
            seed_range[0],
            seed_range[1],
            seed_range[1],
        )

        # start with first seed in range
        next_seed = range_start

        # continue until all parts of seed range are covered
        while next_seed <= range_start + range_length:
            # perform transormation steps for current seed value
            current_val = next_seed
            for map_section in maps:
                for map_range in map_section:
                    if current_val in range(map_range[1], map_range[1] + map_range[2]):
                        current_val = current_val - (map_range[1] - map_range[0])
                        # update skip value to next range: either end of seed range or end of current map range
                        # only the first value of each mapping range needs to be traced since the mapping is linear
                        current_skip = min(
                            current_skip,  # end of available seeds
                            map_range[1] + map_range[2] - current_val,  # mapping range
                        )
                        # but skip at least one
                        current_skip = max(current_skip, 1)
                        break

            destinations.append(current_val)
            next_seed += current_skip
            current_skip = range_length - next_seed + range_start

    return min(destinations)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} input_file")
        exit(1)

    lines = []
    with open(sys.argv[1], "r") as f:
        lines = f.readlines()

    print(calculate_ranges(lines))
