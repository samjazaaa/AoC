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


def calculate_possible(lines):
    cleared_lines = []

    for line in lines:
        cleared_lines.append(line.replace("\n", ""))

    games = parse_games(cleared_lines)

    max_red = 12
    max_green = 13
    max_blue = 14
    possible_sum = 0
    for game in games:
        error = False

        for pull in game["pulls"]:
            if (
                pull["red"] > max_red
                or pull["green"] > max_green
                or pull["blue"] > max_blue
            ):
                error = True
                break

        if not error:
            possible_sum += game["id"]

    return possible_sum


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} input_file")
        exit(1)

    lines = []
    with open(sys.argv[1], "r") as f:
        lines = f.readlines()

    print(calculate_possible(lines))
