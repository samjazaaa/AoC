import sys


def parse_cards(lines):
    cards = []

    for line in lines:
        id_string, numbers = line.split(": ")
        id = int(id_string.replace("Card ", ""))
        winning_string, own_string = numbers.split(" | ")
        winning_numbers = list(
            map(lambda n: int(n), winning_string.strip().replace("  ", " ").split(" "))
        )
        own_numbers = list(
            map(lambda n: int(n), own_string.strip().replace("  ", " ").split(" "))
        )
        cards.append({"id": id, "winning": winning_numbers, "own": own_numbers})

    return cards


def calculate_winning(lines):
    cleared_lines = []

    for line in lines:
        cleared_lines.append(line.replace("\n", ""))

    cards = parse_cards(cleared_lines)

    total_points = 0

    for card in cards:
        card_matches = 0
        for number in card["own"]:
            if number in card["winning"]:
                card_matches += 1

        if card_matches > 0:
            total_points += 2 ** (card_matches - 1)

    return total_points


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} input_file")
        exit(1)

    lines = []
    with open(sys.argv[1], "r") as f:
        lines = f.readlines()

    print(calculate_winning(lines))
