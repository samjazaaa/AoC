import sys


class Valve:
    def __init__(self, name, flow, neighbors):
        self.name = name
        self.flow = flow
        self.neighbors = neighbors

    def __repr__(self) -> str:
        return f"{self.name}: {self.flow} -> {self.neighbors}"


def parse_valves(lines):
    valves = {}

    for line in lines:
        name = line[6:8]
        remainder = line[23:]
        flow_string, remainder = remainder.split(";")
        flow = int(flow_string)
        neighbors = (
            remainder.replace("\n", "")
            .replace(" tunnels lead to valves ", "")
            .replace(" tunnel leads to valve ", "")
            .split(", ")
        )
        valve = Valve(name, flow, neighbors)
        valves[name] = valve

    return valves


def floyd_warshall(valves):
    shortest_ways = {}

    # initialize lookup table
    for name, valve in valves.items():
        neighbors = valve.neighbors
        for other_name, other_valve in valves.items():

            # distance to self is 0
            if other_name == name:
                shortest_ways[(name, name)] = 0
                continue

            # distance to neighbors is 1
            if other_name in neighbors:
                shortest_ways[(name, other_name)] = 1
                continue

            # no direct connection => "infinity"
            shortest_ways[(name, other_name)] = len(valves) + 42  # "infinity"

    # floyd warshall algorithm
    for k in valves.keys():
        for i in valves.keys():
            for j in valves.keys():
                if (
                    shortest_ways[(i, j)] < 0
                    or shortest_ways[(i, j)]
                    > shortest_ways[(i, k)] + shortest_ways[(k, j)]
                ):
                    shortest_ways[(i, j)] = (
                        shortest_ways[(i, k)] + shortest_ways[(k, j)]
                    )

    return shortest_ways


def open_valves(
    current_valve,
    current_flow,
    current_rate,
    unvisited,
    expired,
    valves,
    shortest_ways,
    results,
):

    # check if all (relevant) valves have been visited yet
    if len(unvisited) == 0:
        # calculate remaining flow ticks
        remaining_time = 30 - expired
        results.append(current_flow + current_rate * remaining_time)
        return

    for unvisited_valve in unvisited:
        distance = shortest_ways[(current_valve, unvisited_valve)]
        time_to_open = distance + 1

        # check if valve can be reached within time
        if time_to_open + expired > 30:
            # not reachable => calculate remaining ticks
            remaining_time = 30 - expired
            results.append(current_flow + current_rate * remaining_time)
            # continue checking other unvisited valves
            continue

        new_flow = current_flow + current_rate * time_to_open
        new_rate = current_rate + valves[unvisited_valve].flow
        new_unvisited = list(
            filter(lambda valve: valve != unvisited_valve, unvisited)
        )
        open_valves(
            unvisited_valve,
            new_flow,
            new_rate,
            new_unvisited,
            expired + time_to_open,
            valves,
            shortest_ways,
            results,
        )

    pass


def calculate_pressure(lines):

    valves = parse_valves(lines)

    shortest_ways = floyd_warshall(valves)

    starting_valve = "AA"
    starting_flow = 0
    starting_rate = 0
    starting_time = 0

    relevant_valves = [
        name for name, valve in valves.items() if valve.flow > 0
    ]

    results = []

    open_valves(
        starting_valve,
        starting_flow,
        starting_rate,
        relevant_valves,
        starting_time,
        valves,
        shortest_ways,
        results,
    )

    return max(results)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} input_file")
        exit(1)

    lines = []
    with open(sys.argv[1], "r") as f:
        lines = f.readlines()

    print(calculate_pressure(lines))
