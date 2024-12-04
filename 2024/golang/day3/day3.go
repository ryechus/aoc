package main

import (
	"fmt"
	"regexp"
	"strconv"
	"strings"
)

func partOne(s []string) {
	func_re := regexp.MustCompile(`mul\((?<x>\d{1,3}),(?<y>\d{1,3})\)`)
	output := s
	total := 0

	for _, val := range output {
		matches := func_re.FindAllStringSubmatch(val, -1)

		for _, match := range matches {
			x, _ := strconv.Atoi(match[1])
			y, _ := strconv.Atoi(match[2])

			total += x * y
		}
	}

	fmt.Println(total)
}

func partTwo(s []string) {
	splitter_re := regexp.MustCompile(`(don't\(\)|do\(\))`)
	new_full_txt := ""
	start := 0
	enabled := true

	output := strings.Join(s, "")

	indexes := splitter_re.FindAllStringIndex(output, -1)

	for _, idx := range indexes {
		if enabled {
			new_full_txt += output[start:idx[0]]
		}

		if idx[1]-idx[0] == 4 {
			enabled = true
			start = idx[1]
		} else if idx[1]-idx[0] == 7 {
			enabled = false
			start = idx[1]
		}
		start = idx[1]
	}

	partOne([]string{new_full_txt})
}

func main() {
	output := getOutput()
	partOne(output)
	partTwo(output)
}
