from collections import Counter

from utils import get_file_output

output = get_file_output("day1.txt")

list1 = []
list2 = []
for line in output:
    numbers = line.strip().split(" ")
    list1.append(int(numbers[0]))
    list2.append(int(numbers[-1]))


def part1():
    list1.sort()
    list2.sort()

    total_distance = 0
    i = 0
    while i < len(list1):
        total_distance += abs(list1[i] - list2[i])
        i += 1

    print(total_distance)


def part2():
    counts = Counter(list2)
    i = 0
    total_value = 0
    while i < len(list1):
        value = list1[i]
        new_value = 0
        if value in counts:
            new_value = value * counts[value]

        total_value += new_value
        i += 1

    print(total_value)

if __name__ == '__main__':
    part1()
    part2()
