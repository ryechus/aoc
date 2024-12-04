import re
from itertools import product

from utils import get_file_output


PAD = 3
LINE_LEN = 140
output = get_file_output("day4.txt")
lines = [["-"] * (LINE_LEN + (PAD * 2))] * (PAD * 2)
starting_row = PAD
for line in output:
    lines.insert(starting_row, (["-"] * PAD) + list(line.strip()) + (["-"] * PAD))
    starting_row += 1

# lines.extend([(["-"] * (LINE_LEN + (PAD * 2)))] * PAD)


def find_num_instances_sequential(substr: str, grid: list[list], pos: tuple):
    # search left
    left_value = grid[pos[0]][pos[1]] + grid[pos[0]][pos[1] - 1] + grid[pos[0]][pos[1] - 2] + grid[pos[0]][pos[1] - 3]
    # search right
    right_value = grid[pos[0]][pos[1]] + grid[pos[0]][pos[1] + 1] + grid[pos[0]][pos[1] + 2] + grid[pos[0]][pos[1] + 3]
    # search up
    up_value = grid[pos[0]][pos[1]] + grid[pos[0] - 1][pos[1]] + grid[pos[0] - 2][pos[1]] + grid[pos[0] - 3][pos[1]]
    # search down
    down_value = grid[pos[0]][pos[1]] + grid[pos[0] + 1][pos[1]] + grid[pos[0] + 2][pos[1]] + grid[pos[0] + 3][pos[1]]
    # search top left
    top_left_value = grid[pos[0]][pos[1]] + grid[pos[0] - 1][pos[1] - 1] + grid[pos[0] - 2][pos[1] - 2] + grid[pos[0] - 3][pos[1] - 3]
    # search top right
    top_right_value = grid[pos[0]][pos[1]] + grid[pos[0] - 1][pos[1] + 1] + grid[pos[0] - 2][pos[1] + 2] + grid[pos[0] - 3][pos[1] + 3]
    # search bottom left
    bottom_left_value = (grid[pos[0]][pos[1]] + grid[pos[0] + 1][pos[1] - 1] + grid[pos[0] + 2][pos[1] - 2] + grid[pos[0] + 3][pos[1] - 3])  # noqa
    # search bottom right
    bottom_right_value = (grid[pos[0]][pos[1]] + grid[pos[0] + 1][pos[1] + 1] + grid[pos[0] + 2][pos[1] + 2] + grid[pos[0] + 3][pos[1] + 3])  # noqa

    values = {
        "left_value": 1 if left_value == substr else 0,
        "right_value": 1 if right_value == substr else 0,
        "up_value": 1 if up_value == substr else 0,
        "down_value": 1 if down_value == substr else 0,
        "bottom_left_value": 1 if bottom_left_value == substr else 0,
        "bottom_right_value": 1 if bottom_right_value == substr else 0,
        "top_left_value": 1 if top_left_value == substr else 0,
        "top_right_value": 1 if top_right_value == substr else 0,
    }

    return sum(values.values())


def find_num_instances_crossed(substr: str, grid: list[list], pos: tuple):
    left_diag_coords = [(pos[0] - 1, pos[1] - 1), (pos[0], pos[1]), (pos[0] + 1, pos[1] + 1)]
    right_diag_coords = [(pos[0] + 1, pos[1] - 1), (pos[0], pos[1]), (pos[0] - 1, pos[1] + 1)]
    left_diag = "".join([grid[x][y] for x,y in left_diag_coords])
    right_diag = "".join([grid[x][y] for x,y in right_diag_coords])

    values = {
        "left_diag": 1 if (left_diag == substr or left_diag == substr[::-1]) else 0,
        "right_diag": 1 if (right_diag == substr or right_diag == substr[::-1]) else 0,
    }

    return sum(values.values()) == 2


def part_one():
    total = 0
    for x, y in product(range(PAD, LINE_LEN + PAD), range(PAD, LINE_LEN + PAD)):
       total += find_num_instances_sequential("XMAS", lines, (x, y))

    print(total)


def part_two():
    total = 0
    for x, y in product(range(PAD, LINE_LEN + PAD), range(PAD, LINE_LEN + PAD)):
       total += 1 if find_num_instances_crossed("MAS", lines, (x, y)) else 0

    print(total)



if __name__ == '__main__':
    part_one()
    part_two()
