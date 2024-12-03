from utils import get_file_output

output = get_file_output("day2.txt")
lines = []
for line in output:
    lines.append(line.strip().split(" "))

def is_line_safe(arr):
    unsafe = False
    first_num = int(arr[0])
    second_num = int(arr[1])
    increasing = first_num < second_num

    i = 0
    while i < len(arr):
        if i == len(arr) - 1:
            break

        this_num = int(arr[i])
        next_num = int(arr[i+1])
        if increasing:
            if this_num < next_num:
                if 1 <= next_num - this_num <= 3:
                    ...
                else:
                    unsafe = True
                    break
            else:
                unsafe = True
                break
        else:
            if this_num > next_num:
                if 1 <= this_num - next_num <= 3:
                    ...
                else:
                    unsafe = True
                    break
            else:
                unsafe = True
                break

        i += 1

    return not unsafe


def part1():
    num_safe = 0
    num_unsafe = 0
    for arr in lines:
        safe = is_line_safe(arr)

        if safe:
            num_safe += 1
        else:
            num_unsafe += 1

    print("safe: ", num_safe)
    print("unsafe: ", num_unsafe)


def unsafe_retry(starting_idx, arr):
    while starting_idx < len(arr):
        new_arr = arr.copy()
        new_arr.pop(starting_idx)

        safe = is_line_safe(new_arr)
        if safe:
            return True
        else:
            starting_idx += 1

    return False


def part2():
    num_safe = 0
    num_unsafe = 0
    for arr in lines:
        safe = is_line_safe(arr)

        if not safe:
            safe = unsafe_retry(0, arr)

        if safe:
            num_safe += 1
        else:
            num_unsafe += 1

    print("safe: ", num_safe)
    print("unsafe: ", num_unsafe)


if __name__ == '__main__':
    part1()
    part2()
