import sys


def increase_binary(operands):
    for i in range(len(operands) - 1, -1, -1):
        if operands[i] == 0:
            operands[i] = 1
            return
        elif operands[i] == 1:
            operands[i] = 0


def is_solved(res, ops, operands):
    acc = ops[0]
    for i in range(1, len(ops)):
        if operands[i - 1] == 0:
            acc += ops[i]
        elif operands[i - 1] == 1:
            acc *= ops[i]

    return res == acc


def is_solvable(equation):
    res = equation[0]
    ops = equation[1]

    operands = [0 for _ in range(len(ops) - 1)]

    while True:
        if is_solved(res, ops, operands):
            return True

        if all(map(lambda v: v == 1, operands)):
            break

        increase_binary(operands)

    return False


def calculate_operators(lines):
    cleared_lines = []

    for line in lines:
        cleared_lines.append(line.replace("\n", ""))

    operator_sum = 0
    equations = []

    for line in cleared_lines:
        res_str, operand_str = line.split(": ")
        res = int(res_str)
        ops = [int(op) for op in operand_str.split(" ")]
        equations.append((res, ops))

    for eq in equations:
        if is_solvable(eq):
            operator_sum += eq[0]

    return operator_sum


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} input_file")
        exit(1)

    lines = []
    with open(sys.argv[1], "r") as f:
        lines = f.readlines()

    print(calculate_operators(lines))
