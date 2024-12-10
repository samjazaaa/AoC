import sys


def print_elements(elements):
    for el in elements:
        if el["type"] == "b":
            print(f"block: {el}")
        else:
            print(f"space: {el}")


def calculate_checksum(elements):
    checksum = 0
    for el in elements:
        if el["type"] == "b":
            b_id = el["id"]
            pos = el["start"]
            for _ in range(el["len"]):
                checksum += pos * b_id
                pos += 1

    return checksum


def defrag_block(id, elements):
    for i in range(len(elements) - 1, -1, -1):
        if elements[i]["type"] == "b" and elements[i]["id"] == id:
            block_index = i
    block_entry = elements[block_index]
    block_pos = block_entry["start"]
    block_len = block_entry["len"]
    block_id = block_entry["id"]

    fitting_space_index = -1
    for i, el in enumerate(elements):
        if el["type"] == "b":
            continue
        if el["len"] >= block_len:
            fitting_space_index = i
            break

    if fitting_space_index != -1:
        space_el = elements[fitting_space_index]
        # replace space with block element (and left space element)
        diff = 0
        if space_el["len"] == block_len:
            space_el["type"] = "b"
            space_el["id"] = block_id
        else:  # space is larger than block
            block_entry["start"] = space_el["start"]
            space_el["start"] = space_el["start"] + block_len
            space_el["len"] = space_el["len"] - block_len
            elements.insert(fitting_space_index, block_entry)
            diff = 1

        # remove original block element
        del elements[block_index + diff]  # optional +1 if we added an element


# TODO result is too high
def calculate_fragmentation(lines):
    cleared_lines = []

    for line in lines:
        cleared_lines.append(line.replace("\n", ""))

    disk_map = [int(c) for c in cleared_lines[0]]

    last_is_block = len(disk_map) % 2 != 0
    if not last_is_block:
        disk_map = disk_map[:-1]

    disk_elements = []
    current_pos = 0
    for i, entry in enumerate(disk_map):
        is_block = i % 2 == 0
        if is_block:
            block_id = i // 2
            disk_elements.append(
                {"type": "b", "id": block_id, "start": current_pos, "len": entry}
            )
        else:
            if entry != 0:
                disk_elements.append({"type": "s", "start": current_pos, "len": entry})
        current_pos += entry

    last_id = len(disk_map) // 2
    for id in range(last_id, -1, -1):
        # print(f"defragging id {id}")
        defrag_block(id, disk_elements)
        # print_elements(disk_elements)

    print_elements(disk_elements)
    checksum = calculate_checksum(disk_elements)

    return checksum


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} input_file")
        exit(1)

    lines = []
    with open(sys.argv[1], "r") as f:
        lines = f.readlines()

    print(calculate_fragmentation(lines))
