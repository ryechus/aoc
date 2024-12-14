from functools import reduce, partial
from itertools import permutations, combinations_with_replacement, zip_longest, chain
from operator import mul, add

from utils import get_file_output


CHARS = [mul, add]


def reducer(a, b):
    ...


def part_one(inp: list):
    for _in in inp:
        size = len(_in[1])
        total = _in[0]
        combos = combinations_with_replacement(CHARS, size - 1)
        for combo in combos:
            equation = zip_longest(_in[1], combo)
            func = None
            next_partials = []
            next_args = []
            value = 1
            for idx, part in enumerate(equation):
                next_partials.insert(0, part[1])
                next_args.insert(0, part[0])
                if not func:
                    func = partial(next_partials.pop(), next_args.pop())
                else:
                    value += func(next_args.pop())
                    func = 0
                ...
        ...
    ...


def part_two():
    ...


output = get_file_output("day7.txt")
problem_input = []

for line in output:
    full_line = line.strip()
    line_total, numbers = full_line.split(": ")
    problem_input.append([int(line_total), list(map(int, numbers.split(" ")))])


if __name__ == '__main__':
    part_one(problem_input)
    part_two()

    print(problem_input)