package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"slices"
	"strconv"
	"strings"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func getOutput() ([]int, []int) {
	f, err := os.Open("input/day1.txt")

	check(err)
	scanner := bufio.NewScanner(f)
	list1 := make([]int, 0)
	list2 := make([]int, 0)

	for scanner.Scan() {
		line := scanner.Text()
		trimmed_line := strings.Trim(line, " ")
		split_line := strings.Split(trimmed_line, " ")
		last_index := len(split_line) - 1

		first_number, _ := strconv.Atoi(split_line[0])
		second_number, _ := strconv.Atoi(split_line[last_index])

		list1 = append(list1, first_number)
		list2 = append(list2, second_number)
	}

	return list1, list2
}

func partOne() {
	list1, list2 := getOutput()

	slices.Sort(list1)
	slices.Sort(list2)

	total_distance := 0

	i := 0

	for i < len(list1) {
		diff := list1[i] - list2[i]
		total_distance += int(math.Abs(float64(diff)))

		i += 1
	}

	fmt.Println(total_distance)
}

func partTwo() {
	list1, list2 := getOutput()
	counts := map[int]int{}

	for _, num := range list2 {
		counts[num] += 1
	}

	total_value := 0

	for _, num := range list1 {
		count, ok := counts[num]
		new_value := 0
		if ok {
			new_value = num * count
		}

		total_value += new_value
	}

	fmt.Println(total_value)
}

func main() {
	partOne()
	partTwo()
}
