import sys


def parse_pull_string(pull_string):
    pull = {"red": 0, "green": 0, "blue": 0}

    for part in pull_string.split(", "):
        number, color = part.split(" ")
        pull[color] = int(number)

    return pull


def parse_game_line(line):
    id_string, remainder = line.split(": ")
    id = int(id_string.replace("Game ", ""))

    pull_strings = remainder.split("; ")
    pulls = []
    for pull_string in pull_strings:
        pull = parse_pull_string(pull_string)
        pulls.append(pull)

    return {"id": id, "pulls": pulls}


def parse_games(lines):
    games = []

    for line in lines:
        game = parse_game_line(line)
        games.append(game)

    return games


def calculate_power(lines):
    cleared_lines = []

    for line in lines:
        cleared_lines.append(line.replace("\n", ""))

    games = parse_games(cleared_lines)

    power_sum = 0
    for game in games:
        min_red = 0
        min_green = 0
        min_blue = 0

        for pull in game["pulls"]:
            min_red = max(min_red, pull["red"])
            min_green = max(min_green, pull["green"])
            min_blue = max(min_blue, pull["blue"])

        power_sum += min_red * min_green * min_blue

    return power_sum


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} input_file")
        exit(1)

    lines = []
    with open(sys.argv[1], "r") as f:
        lines = f.readlines()

    print(calculate_power(lines))
