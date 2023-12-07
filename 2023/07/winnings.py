import sys
from functools import cmp_to_key

order = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"][::-1]


def parse_hands(lines):
    hands = []

    for line in lines:
        cards, bid = line.split(" ")
        hands.append((cards, int(bid)))

    return hands


def is_five(cards):
    return all(map(lambda c: c == cards[0], cards))


def is_four(cards):
    return cards.count(cards[0]) == 4 or cards.count(cards[1]) == 4


def is_full_house(cards):
    sorted_cards = sorted(cards)
    first_count = sorted_cards.count(sorted_cards[0])
    second_count = sorted_cards.count(sorted_cards[4])
    return (first_count == 3 and second_count == 2) or (
        first_count == 2 and second_count == 3
    )


def is_three(cards):
    for c in cards:
        if cards.count(c) == 3:
            return True
    return False


def is_double_pair(cards):
    first_symbol = ""
    for c in cards:
        if cards.count(c) == 2:
            if first_symbol == "" or first_symbol == c:
                first_symbol = c
            else:
                return True
    return False


def is_pair(cards):
    for c in cards:
        if cards.count(c) == 2:
            return True
    return False


def compare_first(first_cards, second_cards):
    for a, b in zip(first_cards, second_cards):
        index_a = order.index(a)
        index_b = order.index(b)
        if index_a == index_b:
            continue
        if index_a > index_b:
            return 1
        elif index_b > index_a:
            return -1
    return 0


def rank_cards(cards):
    if is_five(cards):
        return 6
    if is_four(cards):
        return 5
    if is_full_house(cards):
        return 4
    if is_three(cards):
        return 3
    if is_double_pair(cards):
        return 2
    if is_pair(cards):
        return 1

    return 0


def compare_hands(first, second):
    first_rank = rank_cards(first[0])

    second_rank = rank_cards(second[0])

    if first_rank > second_rank:
        return 1
    if second_rank > first_rank:
        return -1

    # equal type
    return compare_first(first[0], second[0])


def calculate_winnings(lines):
    cleared_lines = []

    for line in lines:
        cleared_lines.append(line.replace("\n", ""))

    hands = parse_hands(cleared_lines)

    hands.sort(key=cmp_to_key(compare_hands))

    winnings = 0
    for i, hand in enumerate(hands):
        winnings += (i + 1) * hand[1]

    return winnings


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} input_file")
        exit(1)

    lines = []
    with open(sys.argv[1], "r") as f:
        lines = f.readlines()

    print(calculate_winnings(lines))
