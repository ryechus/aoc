package main

func isLineSafe(line []int) bool {
	unsafe := false
	first_num := line[0]
	second_num := line[1]
	is_increasing := first_num < second_num

	for i := 0; i < len(line); i++ {
		if i == len(line)-1 {
			break
		}

		this_num := line[i]
		next_num := line[i+1]

		if is_increasing {
			diff := next_num - this_num
			if this_num < next_num {
				if 1 <= diff && diff <= 3 {
					continue
				} else {
					unsafe = true
					break
				}
			} else {
				unsafe = true
				break
			}
		} else {
			diff := this_num - next_num
			if this_num > next_num {
				if 1 <= diff && diff <= 3 {
					continue
				} else {
					unsafe = true
					break
				}
			} else {
				unsafe = true
				break
			}
		}
	}
	return !unsafe
}

func unsafeRetry(starting_idx int, arr []int) bool {
	for i := starting_idx; i < len(arr); i++ {
		new_arr := make([]int, len(arr))

		copy(new_arr, arr)
		new_arr = append(new_arr[:i], new_arr[i+1:]...)

		safe := isLineSafe(new_arr)
		if safe {
			return true
		}
	}
	return false
}
