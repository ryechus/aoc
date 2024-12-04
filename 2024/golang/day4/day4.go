package main

import (
	"fmt"
	"slices"
	"strings"

	"github.com/schwarmco/go-cartesian-product"
)

const PAD = 3
const LINE_LEN = 140

func reverseString(s string) string {
	str_rune := []rune(s)

	for i, j := 0, len(str_rune)-1; i < j; i, j = i+1, j-1 {
		str_rune[i], str_rune[j] = str_rune[j], str_rune[i]
	}

	result := string(str_rune)
	return result
}

func find_num_instances_sequential(substr string, grid [][]string, pos Pair) int {
	left_value := grid[pos.y][pos.x] + grid[pos.y][pos.x-1] + grid[pos.y][pos.x-2] + grid[pos.y][pos.x-3]
	right_value := grid[pos.y][pos.x] + grid[pos.y][pos.x+1] + grid[pos.y][pos.x+2] + grid[pos.y][pos.x+3]
	bottom_value := grid[pos.y][pos.x] + grid[pos.y+1][pos.x] + grid[pos.y+2][pos.x] + grid[pos.y+3][pos.x]
	top_value := grid[pos.y][pos.x] + grid[pos.y-1][pos.x] + grid[pos.y-2][pos.x] + grid[pos.y-3][pos.x]
	top_left_value := grid[pos.y][pos.x] + grid[pos.y-1][pos.x-1] + grid[pos.y-2][pos.x-2] + grid[pos.y-3][pos.x-3]
	top_right_value := grid[pos.y][pos.x] + grid[pos.y-1][pos.x+1] + grid[pos.y-2][pos.x+2] + grid[pos.y-3][pos.x+3]
	bottom_left_value := grid[pos.y][pos.x] + grid[pos.y+1][pos.x-1] + grid[pos.y+2][pos.x-2] + grid[pos.y+3][pos.x-3]
	bottom_right_value := grid[pos.y][pos.x] + grid[pos.y+1][pos.x+1] + grid[pos.y+2][pos.x+2] + grid[pos.y+3][pos.x+3]

	total := 0
	if left_value == substr {
		total += 1
	}
	if right_value == substr {
		total += 1
	}
	if bottom_value == substr {
		total += 1
	}
	if top_value == substr {
		total += 1
	}
	if top_left_value == substr {
		total += 1
	}
	if top_right_value == substr {
		total += 1
	}
	if bottom_left_value == substr {
		total += 1
	}
	if bottom_right_value == substr {
		total += 1
	}

	return total
}

func do_instances_cross(substr string, grid [][]string, pos Pair) bool {
	left_diag_value := grid[pos.y-1][pos.x-1] + grid[pos.y][pos.x] + grid[pos.y+1][pos.x+1]
	right_diag_value := grid[pos.y+1][pos.x-1] + grid[pos.y][pos.x] + grid[pos.y-1][pos.x+1]

	total := 0

	if left_diag_value == substr || left_diag_value == reverseString(substr) {
		total += 1
	}
	if right_diag_value == substr || right_diag_value == reverseString(substr) {
		total += 1
	}

	return total == 2
}

func getCartesian() chan []interface{} {
	x := make([]interface{}, 0)
	for n := range LINE_LEN {
		x = append(x, n+PAD)
	}

	coords := cartesian.Iter(x, x)

	return coords
}

func partOne(input [][]string) {
	coords := getCartesian()

	total := 0
	for product := range coords {
		pair := Pair{x: product[0].(int), y: product[1].(int)}
		total += find_num_instances_sequential("XMAS", input, pair)
	}

	fmt.Println(total)
}

func partTwo(input [][]string) {
	coords := getCartesian()

	total := 0
	for product := range coords {
		pair := Pair{x: product[0].(int), y: product[1].(int)}
		if do_instances_cross("MAS", input, pair) {
			total += 1
		}
	}

	fmt.Println(total)
}

func main() {
	blank_line := slices.Repeat([]string{"-"}, LINE_LEN+(PAD*2))
	blank_lines := slices.Repeat([][]string{blank_line}, (PAD * 2))
	starting_row := PAD
	output := getOutput()
	for _, val := range output {
		next_line := slices.Repeat([]string{"-"}, PAD)
		next_line = append(next_line, strings.Split(val, "")...)
		next_line = append(next_line, slices.Repeat([]string{"-"}, PAD)...)
		blank_lines = slices.Insert(blank_lines, starting_row, next_line)
		starting_row += 1
	}

	partOne(blank_lines)
	partTwo(blank_lines)
}
