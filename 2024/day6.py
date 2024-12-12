from collections import namedtuple
from time import time, sleep

from utils import get_file_output


output = get_file_output("day6.txt")
instructions = []
direction_changes = ["up",]
Point = namedtuple("Point", "y x")
O_CHAR = "#"


class CycleException(Exception):
    ...


CACHE = {}


class MemoryObject:
    def __init__(self, value):
        if tuple(value) not in CACHE:
            CACHE[tuple(value)] = self
        self.value = Point(*value)
        self.next = None

for idx, line in enumerate(output):
    _line = line.strip()
    start_col = _line.find("^")
    if start_col > 0:
        STARTING_POSITION = MemoryObject((idx, start_col))
    instructions.append(list(line.strip()))


def is_obstacle(pos: MemoryObject, ins):
    value = pos.value
    char = ins[value[0]][value[1]]
    if char == O_CHAR:
        return True

    return False


def get_next_position(direction: str, pos: MemoryObject) -> MemoryObject:
    value = pos.value
    if direction == "up":
        return MemoryObject((value[0] - 1, value[1]))
    if direction == "right":
        return MemoryObject((value[0], value[1] + 1))
        # value[1] += 1
    if direction == "down":
        # value[0] += 1
        return MemoryObject((value[0] + 1, value[1]))
    if direction == "left":
        # value[1] -= 1
        return MemoryObject((value[0], value[1] - 1))


def change_direction(direction):
    if direction == "up":
        direction = "right"
    elif direction == "right":
        direction = "down"
    elif direction == "down":
        direction = "left"
    elif direction == "left":
        direction = "up"

    # print(f"changed directions {direction}")
    direction_changes.append(direction)

    return direction


def print_output(instruction_set, visited_locations):
    for visited_location in visited_locations:
        instruction_set[visited_location[0]][visited_location[1]] = "X"
        ...

    with open("output/day6.txt", "w+") as f:
        for ins in instruction_set:
            o = "".join(ins)
            o += "\n"
            f.write(o)



def part_one(starting_position, instruction_set, check_cycles=False):
    direction = "up"
    first_position = position = MemoryObject(tuple(starting_position.value))
    visited_locations = set()
    while (position.value[0] >= 0 and
           position.value[1] >= 0 and
           position.value[0] < len(instruction_set) and
           position.value[1] < len(instruction_set[0])
    ):
        if not is_obstacle(position, instruction_set):
            next_position = get_next_position(direction, position)
            position.next = CACHE.get(tuple(next_position.value), next_position)
            previous_position = position
            position = next_position
            visited_locations.add(position.value)
        else:
            direction = change_direction(direction)
            visited_locations.remove(position.value)
            position = previous_position
            # position.next = None

        # if check_cycles:
        #     if detect_cycle(first_position):
        #         # print_output(instruction_set, visited_locations)
        #         return first_position, False

    print(len(visited_locations))
    # print_output(instruction_set, visited_locations)
    return first_position, visited_locations


# Function to detect cycles: Floyd's Cycle Detection Algorithm
def detect_cycle(head: MemoryObject):
    slow = head
    fast = head

    # If fast points to None, then no cyclic reference
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False


def part_two(locations):
    total = 0
    good_obstacles = set()
    for l in locations:
        print(f"Placing obstacle at {l}")
        i_ins = instructions.copy()

        i_ins[l[0]][l[1]] = O_CHAR

        _, success = part_one(STARTING_POSITION, i_ins, check_cycles=True)
        if not success:
            print(f"detected cycle at {l}")
            good_obstacles.add(l)

    print(len(good_obstacles))




if __name__ == '__main__':
    _, _visited_locations = part_one(STARTING_POSITION, instructions)
    # part_two(_visited_locations)
