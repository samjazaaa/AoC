#! /usr/bin/env python3

import sys


def parse_population(line):

    vals = [int(val) for val in line.split(',')]

    population = [0 for _ in range(9)]

    for val in vals:
        population[val] += 1

    return population


def get_population(file_name) -> int:
    input = ""
    with open(file_name, 'r') as f:
        input = f.readline().rstrip()

    population = parse_population(input)

    # perform 80 generations
    current_gen = 0
    for i in range(80):
        new_gen = (current_gen+1) % 9
        population[(new_gen+6) % 9] += population[current_gen]
        current_gen = new_gen

    return sum(population)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: %s <input_file>' % sys.argv[0])
        exit(1)

    print(get_population(sys.argv[1]))
