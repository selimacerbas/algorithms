package main

import "math"

func SortedSquaredArray(array []int) []int {

	lst := make([]int, len(array))

	left_ptr := 0
	right_ptr := len(array) - 1

	for i := len(array) - 1; i >= 0; i-- {

		left_val := array[left_ptr]
		right_val := array[right_ptr]

		if math.Abs(float64(left_val)) > math.Abs(float64(right_val)) {
			lst[i] = int(left_val * left_val)
			left_ptr++
		} else {
			lst[i] = int(right_val * right_val)
			right_ptr--
		}
	}

	return lst

}
