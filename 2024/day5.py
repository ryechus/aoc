from collections import defaultdict

from utils import get_file_output


dependencies = defaultdict(list)
updates = []

output = get_file_output("day5.txt")
for line in output:
    val = line.strip().split("|")
    if val[0] not in dependencies[val[1]]:
        dependencies[val[1]].append(val[0])

output_updates = get_file_output("day5_b.txt")
for l in output_updates:
    updates.append(l.strip().split(","))


def get_midway_point(arr):
    return arr[len(arr)//2]


def part_one(_input):
    total = 0
    valid_updates = []
    invalid_updates = []
    for update in _input:
        is_valid = True
        for idx, n in enumerate(update):
            deps = dependencies[n]
            rest = update[idx + 1:]
            matches = set(deps) & set(rest)
            if matches:
                is_valid = False
                invalid_updates.append(update)
                break

        if is_valid:
            total += int(get_midway_point(update))
            valid_updates.append(update)

    print(total)

    return invalid_updates


def iterative_dfs_improved(graph, start, allowed, seen, stack):
    working_stack = [(start, graph[start])]

    while working_stack:
        v, gen = working_stack.pop()
        seen.add(v)

        for next_neighbor in gen:
            if next_neighbor not in seen:
                working_stack.append((v, gen))
                working_stack.append((next_neighbor, graph[next_neighbor]))
                break
        else:
            if v in allowed:
                stack.append(v)



def part_two(_input):
    # for every update make a queue with the correct order
    total = 0
    reordered = []
    for idx, update in enumerate(_input):
        new_update = []
        for n in update:
            deps = iterative_dfs_improved(dependencies, n)
            print(deps)
            # for d in deps[::-1]:
            #     if d not in seen and d in update:
            #         seen.add(d)
            #         new_update.append(d)

        is_valid = part_one([new_update])
        if is_valid:
            raise Exception(is_valid, update)

        reordered.append(new_update)

    for update in reordered:
        total += int(get_midway_point(update))

    print(total)


if __name__ == '__main__':
    # 97,75,47,29,13
    seen = set()
    update = ['79','65','51','72','41','95','37','24','97','61','13','44','21','38','71','56','17','31','47','62','22','88','19']
    # update = ["1", "2", "3", "4", "5", "6"]
    build_orders = []
    new_update = []
    _seen = set()

    for n in update:
        if n not in _seen:
            iterative_dfs_improved(dependencies, n, update, _seen, new_update)

    is_valid = part_one([new_update])
    if is_valid:
        raise Exception(is_valid, update)
        # build_orders.append(deps)
        # if n not in new_update:
        #     new_update.append(n)
        # idx = new_update.index(n)
        # for d in deps:
        #     if d not in new_update:
        #         new_update.insert(idx, d)

    # level = 0
    # i = 0
    # while True:
    #     b = build_orders[i]
    #     new_update.append(b[level])
    #     i += 0
    #
    #     if i >= len(b):
    #         i = 0
    #         level += 1



    _invalid_updates = part_one(updates)
    # part_two(_invalid_updates)
    # print(updates)
    # print({1,2,3,4} & {4})

    # 4619 too low
    # 4923 too high