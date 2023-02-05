import sys


def print_pixel(cycle, sprite_center):
    # break line for cycle 41, 81, ...
    if cycle % 40 == 1:
        print("")

    line_pos = (cycle-1) % 40

    if line_pos in [sprite_center + x for x in range(-1, 2, 1)]:
        print('#', end='')
        return

    print('.', end='')


def calculate_strength(lines):

    sprite_center = 1
    cycle = 0

    for line in lines:
        if line.replace('\n', '') == 'noop':
            # start the cycle
            cycle += 1
            # print the pixel for current cycle
            print_pixel(cycle, sprite_center)
            # do nothing
            continue

        _, val = line.replace('\n', '').split(' ')
        # start first cycle
        cycle += 1
        # print pixel
        print_pixel(cycle, sprite_center)
        # start second cycle
        cycle += 1
        # print pixel
        print_pixel(cycle, sprite_center)
        # at the end of the second cycle update the value
        sprite_center += int(val)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} input_file")
        exit(1)

    lines = []
    with open(sys.argv[1], "r") as f:
        lines = f.readlines()

    calculate_strength(lines)
    print('')
