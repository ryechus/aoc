package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func getOutput() [][]string {
	f, err := os.Open("../../input/day2.txt")

	check(err)
	scanner := bufio.NewScanner(f)
	list1 := make([][]string, 0)
	// list2 := make([]int, 0)

	for scanner.Scan() {
		line := scanner.Text()
		trimmed_line := strings.Trim(line, " ")
		split_line := strings.Split(trimmed_line, " ")

		list1 = append(list1, split_line)
	}

	return list1
}

func makeInts(arr []string) []int {
	new_arr := make([]int, len(arr))
	for idx, num := range arr {
		casted_number, _ := strconv.Atoi(num)
		new_arr[idx] = casted_number
	}

	return new_arr
}

func partOne() {
	num_safe := 0
	num_unsafe := 0

	for _, line := range getOutput() {
		casted_output := makeInts(line)

		safe := isLineSafe(casted_output)
		if safe {
			num_safe += 1
		} else {
			num_unsafe += 1
		}
	}

	fmt.Printf("safe: %d\n", num_safe)
	fmt.Printf("unsafe: %d\n", num_unsafe)
}

func partTwo() {
	num_safe := 0
	num_unsafe := 0

	for _, line := range getOutput() {
		casted_output := makeInts(line)

		safe := isLineSafe(casted_output)

		if !safe {
			safe = unsafeRetry(0, casted_output)
		}
		if safe {
			num_safe += 1
		} else {
			num_unsafe += 1
		}
	}

	fmt.Printf("safe: %d\n", num_safe)
	fmt.Printf("unsafe: %d\n", num_unsafe)
}

func main() {
	partOne()
	partTwo()
}
