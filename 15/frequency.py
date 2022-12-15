import sys


def parse_sensors(lines):
    sensors = []
    beacons = []

    for line in lines:
        pair = tuple(
            map(
                lambda coords: tuple(
                    map(lambda val: int(val[2:]), coords.split(", "))
                ),
                line.replace("\n", "")
                .replace("Sensor at ", "")
                .split(": closest beacon is at "),
            )
        )
        sensors.append(pair[0])
        beacons.append(pair[1])

    return (sensors, beacons)


def manhattan_distance(first, second):
    distance = 0
    for dimension in zip(first, second):
        distance += abs(dimension[0] - dimension[1])

    return distance


def cover_line(sensor, max_distance, y, covered):

    if y > 4000000 or y < 0:
        return False

    nearest_point = (sensor[0], y)

    if manhattan_distance(sensor, nearest_point) > max_distance:
        return False

    covered.add(nearest_point)

    width = 1
    while (
        manhattan_distance(sensor, (sensor[0] + width, y))
        <= max_distance
    ):
        print(f"y: {y}, width: {width}")
        covered.add((sensor[0] + width, y))
        covered.add((sensor[0] - width, y))
        width += 1
        if sensor[0] + width > 4000000 or sensor[0] - width < 0:
            break

    return True


def calculate_frequency(lines):

    sensors, beacons = parse_sensors(lines)
    coverage_distances = [
        manhattan_distance(sensor, beacon)
        for sensor, beacon in zip(sensors, beacons)
    ]

    # coordinates covered by sensors
    covered = set()

    sensor_count = len(sensors)
    current = 1

    # check each sensor if straight connection <= coverage distance
    for sensor, max_distance in zip(sensors, coverage_distances):
        print(f"scanning sensor {current}/{sensor_count}")

        # TODO no need to calc distance: add a list (?) for each line to covered set and make it 2 shorter for every y step

        current += 1

        # add all covered points on same height
        cover_line(sensor, max_distance, sensor[1], covered)

        # symmetrically expand up and down
        height = 1
        while cover_line(sensor, max_distance, sensor[1]+height, covered):
            cover_line(sensor, max_distance, sensor[1]-height, covered)
            height += 1

    max_val = 4000000

    print(covered)
    for y in range(max_val+1):
        for x in range(max_val+1):
            if (x, y) not in covered:
                return x*4000000 + y

    return len(covered)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} input_file")
        exit(1)

    lines = []
    with open(sys.argv[1], "r") as f:
        lines = f.readlines()

    print(calculate_frequency(lines))
