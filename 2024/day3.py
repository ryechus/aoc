import re

from utils import get_file_output

FUNC_RE = re.compile(r"mul\((?P<x>\d{1,3}),(?P<y>\d{1,3})\)")
SPLITTER_RE = re.compile(r"(don't\(\)|do\(\))")


output = get_file_output("day3.txt")
lines = []
for line in output:
    lines.append(line.strip())


def part_one():
    total = 0
    for txt in lines:
        results = re.findall(FUNC_RE, txt)
        for result in results:
            total += int(result[0]) * int(result[1])

    print(total)


def part_two():
    total = 0
    new_full_txt = ""
    enabled = True
    for txt in lines:
        tokens = SPLITTER_RE.split(txt)
        for token in tokens:
            if token == "don't()":
                enabled = False
            elif token == "do()":
                enabled = True
                continue

            if enabled:
                new_full_txt += token
                continue

    results = re.findall(FUNC_RE, new_full_txt)
    for result in results:
        total += int(result[0]) * int(result[1])

    print(total)


if __name__ == '__main__':
    part_one()
    part_two()
