import sys


def calculate_compact(lines):
    cleared_lines = []

    for line in lines:
        cleared_lines.append(line.replace("\n", ""))

    disk_map = [int(c) for c in cleared_lines[0]]

    last_is_block = len(disk_map) % 2 != 0
    if not last_is_block:
        disk_map = disk_map[:-1]
    last_id = len(disk_map) // 2

    # pos in map is always id*2

    next_map_pos = 1
    next_disk_pos = disk_map[0]
    space_left = disk_map[next_map_pos]

    next_skipped_id = 1

    next_moved_id = last_id
    next_moved_map_pos = next_moved_id * 2

    left_to_move = disk_map[next_moved_map_pos]

    checksum = 0

    while next_map_pos < next_moved_map_pos:
        while space_left > 0 and left_to_move > 0:
            # print(f"moving 1 block of id {next_moved_id} to disk pos {next_disk_pos}")
            space_left -= 1
            left_to_move -= 1
            # print(f"adding to sum: p {next_disk_pos} * id {next_moved_id}")
            checksum += next_disk_pos * next_moved_id
            next_disk_pos += 1

        if space_left == 0:
            # increase next free map pos (now on block!)
            next_map_pos += 1
            if next_map_pos == next_moved_map_pos:
                for _ in range(left_to_move):
                    # print(f"xadding to sum: p {next_disk_pos} * id {next_skipped_id}")
                    checksum += next_skipped_id * next_disk_pos
                    next_disk_pos += 1
                break
            # process next skip id (id*next_free_disk_pos) "*len of block" (remember to inc free disk pos)
            block_len = disk_map[next_map_pos]
            for _ in range(block_len):
                # print(f"adding to sum: p {next_disk_pos} * id {next_skipped_id}")
                checksum += next_skipped_id * next_disk_pos
                next_disk_pos += 1
            # update next skipped id
            next_skipped_id += 1
            # increase next free map pos
            next_map_pos += 1
            # get free space
            space_left = disk_map[next_map_pos]
        if left_to_move == 0:
            next_moved_id -= 1
            next_moved_map_pos -= 2  # skip trailing free space
            left_to_move = disk_map[next_moved_map_pos]

    return checksum


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} input_file")
        exit(1)

    lines = []
    with open(sys.argv[1], "r") as f:
        lines = f.readlines()

    print(calculate_compact(lines))
