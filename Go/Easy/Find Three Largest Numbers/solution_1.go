package main

import "math"

func FindThreeLargestNumbers(array []int) []int {

	lst := []int{math.MinInt32, math.MinInt32, math.MinInt32}

	for _, element := range array {
		updateLargest(lst, element)
	}
	return lst
}

func updateLargest(array []int, element int) {

	if element > array[2] {
		shiftAndUpdate(array, element, 2)
	} else if element > array[1] {
		shiftAndUpdate(array, element, 1)
	} else if element > array[0] {
		shiftAndUpdate(array, element, 0)
	}

}

func shiftAndUpdate(array []int, element int, idx int) {

	for i := 0; i < idx+1; i++ {

		if i == idx {
			array[i] = element
		} else {
			array[i] = array[i+1]
		}
	}
}
