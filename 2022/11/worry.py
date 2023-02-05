import sys
from functools import partial


class Monkey:
    def __init__(self, items=[], op=lambda x: x, test=1, yes=0, no=0):
        self.items = items
        self.op = op
        self.test = test
        self.yes = yes
        self.no = no

        self.inspections = 0

    def __str__(self) -> str:
        return f"""
        items: {self.items},
        test: {self.test},
        yes: {self.yes},
        no: {self.no},
        inspections: {self.inspections}
        """


def calc_worry(current, factor, mult=False):
    if mult:
        if factor == "old":
            return current * current
        return current * int(factor)

    if factor == "old":
        return current + current
    return current + int(factor)


def parse_monkeys(lines):
    monkeys = []

    i = 0
    while i < len(lines):
        if lines[i] == "\n":
            i += 1
            continue

        # parse monkey's starting items
        item_line = (
            lines[i + 1].replace("\n", "").replace("  Starting items: ", "")
        )
        items = [int(item) for item in item_line.split(", ")]

        # parse operation
        operator, val = (
            lines[i + 2]
            .replace("\n", "")
            .replace("  Operation: new = old ", "")
            .split(" ")
        )
        if operator == "*":
            op = partial(calc_worry, factor=val, mult=True)
        if operator == "+":
            op = partial(calc_worry, factor=val, mult=False)

        # parse test
        test = int(
            lines[i + 3].replace("\n", "").replace("  Test: divisible by ", "")
        )

        # parse yes
        yes = int(
            lines[i + 4]
            .replace("\n", "")
            .replace("    If true: throw to monkey ", "")
        )

        # parse no
        no = int(
            lines[i + 5]
            .replace("\n", "")
            .replace("    If false: throw to monkey ", "")
        )

        # create monkey
        monkey = Monkey(items=items, op=op, test=test, yes=yes, no=no)
        monkeys.append(monkey)
        i += 6

    return monkeys


def monkey_round(monkeys, common_factor):
    for monkey in monkeys:
        while len(monkey.items) > 0:
            item = monkey.items.pop(0)
            monkey.inspections += 1

            new_worry = monkey.op(item)
            # new_worry = int(new_worry / 3)
            new_worry = new_worry % common_factor

            if new_worry % monkey.test == 0:
                # yes
                monkeys[monkey.yes].items.append(new_worry)
            else:
                # no
                monkeys[monkey.no].items.append(new_worry)


def calculate_worry(lines):

    monkeys = parse_monkeys(lines)

    factors = set()
    for monkey in monkeys:
        factors.add(monkey.test)

    common_factor = 1
    for factor in factors:
        common_factor *= factor

    for _ in range(10000):
        monkey_round(monkeys, common_factor)

    inspections = [monkey.inspections for monkey in monkeys]
    inspections.sort()

    return inspections[-1] * inspections[-2]


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} input_file")
        exit(1)

    lines = []
    with open(sys.argv[1], "r") as f:
        lines = f.readlines()

    print(calculate_worry(lines))
