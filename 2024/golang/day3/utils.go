package main

import (
	"bufio"
	"os"
	"strings"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func getOutput() []string {
	f, err := os.Open("../../input/day3.txt")

	check(err)
	scanner := bufio.NewScanner(f)
	list1 := make([]string, 0)
	// list2 := make([]int, 0)

	for scanner.Scan() {
		line := scanner.Text()
		trimmed_line := strings.Trim(line, " ")

		list1 = append(list1, trimmed_line)
	}

	return list1
}
