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


def calculate_coverage(lines):

    sensors, beacons = parse_sensors(lines)
    coverage_distances = [
        manhattan_distance(sensor, beacon)
        for sensor, beacon in zip(sensors, beacons)
    ]

    target_height = 10  # TODO change to 2000000 for "production"

    covered = set()  # x coordinates of target line that are covered

    # check each sensor if straight connection <= coverage distance
    for sensor, max_distance in zip(sensors, coverage_distances):
        nearest_point = (sensor[0], target_height)

        if manhattan_distance(sensor, nearest_point) > max_distance:
            continue

        # nearest point is covered => add
        covered.add(sensor[0])

        # symmetrically spread check to both side until distance is too far
        width = 1
        while (
            manhattan_distance(sensor, (sensor[0] + width, target_height))
            <= max_distance
        ):
            covered.add(sensor[0] + width)
            covered.add(sensor[0] - width)
            width += 1

    # remove positions of other beacons
    for position in beacons:
        if position[1] == target_height and position[0] in covered:
            covered.remove(position[0])

    return len(covered)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} input_file")
        exit(1)

    lines = []
    with open(sys.argv[1], "r") as f:
        lines = f.readlines()

    print(calculate_coverage(lines))
