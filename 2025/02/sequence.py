import sys


def calculate_sequence(lines):
    cleared_lines = []

    for line in lines:
        cleared_lines.append(line.replace("\n", ""))

    seq_sum = 0

    ranges = list(map(lambda r: r.split("-"), cleared_lines[0].split(",")))

    for r in ranges:
        for val in range(int(r[0]), int(r[1]) + 1):
            # print(val)
            str_val = str(val)
            str_len = len(str_val)

            for seq_len in range(1, (str_len // 2) + 1):
                # print(f"checking len {seq_len}")
                pattern = str_val[0:seq_len]
                # print(f"pattern: {pattern}")
                check_index = seq_len
                fit = True
                while check_index <= str_len - seq_len:
                    ref = str_val[check_index : check_index + seq_len]
                    # print(f"ref: {ref}")
                    if ref != pattern:
                        fit = False
                        break
                if fit:
                    print(f"{val} has seq_len {seq_len}")
                    seq_sum += val
                    break

    return seq_sum


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} input_file")
        exit(1)

    lines = []
    with open(sys.argv[1], "r") as f:
        lines = f.readlines()

    print(calculate_sequence(lines))
