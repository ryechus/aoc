package main

import (
	"bufio"
	"os"
	"strings"
)

type Pair struct {
	x int
	y int
}

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func getOutput() []string {
	f, err := os.Open("../../input/day4.txt")

	check(err)
	scanner := bufio.NewScanner(f)
	list1 := make([]string, 0)

	for scanner.Scan() {
		line := scanner.Text()
		trimmed_line := strings.Trim(line, " ")

		list1 = append(list1, trimmed_line)
	}

	return list1
}
