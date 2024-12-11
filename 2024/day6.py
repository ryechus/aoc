from utils import get_file_output


output = get_file_output("day6.txt")
instructions = []
position = [0, 0]
visited_locations = set()
DIRECTION = "up"
for idx, line in enumerate(output):
    _line = line.strip()
    start_col = _line.find("^")
    if start_col > 0:
        position = [idx, start_col]
    instructions.append(list(line.strip()))


def is_obstacle(pos):
    char = instructions[pos[0]][pos[1]]
    if char == "#":
        return True

    return False

def change_direction(direction):
    if direction == "up":
        direction = "right"
    elif direction == "right":
        direction = "down"
    elif direction == "down":
        direction = "left"
    elif direction == "left":
        direction = "up"

    print(f"changed directions {direction}")

    return direction



def part_one():
    direction = "up"
    while (position[0] >= 0 and
           position[1] >= 0 and
           position[0] < len(instructions) and
           position[1] < len(instructions[0])
    ):
        if not is_obstacle(position):
            previous_position = [position[0], position[1]]
            if direction == "up":
                position[0] -= 1
            if direction == "right":
                position[1] += 1
            if direction == "down":
                position[0] += 1
            if direction == "left":
                position[1] -= 1
            print(position)
            visited_locations.add(tuple(position))
        else:
            visited_locations.remove(tuple(position))
            direction = change_direction(direction)
            position[0] = previous_position[0]
            position[1] = previous_position[1]

    for visited_location in visited_locations:
        instructions[visited_location[0]][visited_location[1]] = "X"
        ...

    with open("output/day6.txt", "w+") as f:
        for ins in instructions:
            o = "".join(ins)
            o += "\n"
            f.write(o)

    print(len(visited_locations))


def part_two():
    ...


if __name__ == '__main__':
    part_one()
    part_two()
    # print(position)
