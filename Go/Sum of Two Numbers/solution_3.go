package main

import "sort"

// O(nlog(n)) time | O(1) space
func TwoNumberSum(array []int, target int) []int {

	sort.Ints(array)
	first_ptr := 0
	second_ptr := len(array) - 1

	for first_ptr < second_ptr {

		currentSum := array[first_ptr] + array[second_ptr]

		if currentSum == target {
			return []int{array[first_ptr], array[second_ptr]}
		} else if currentSum < target {
			first_ptr += 1
		} else {
			second_ptr -= 1
		}

	}

	return []int{}
}
