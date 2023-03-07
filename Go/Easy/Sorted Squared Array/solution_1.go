package main

import "sort"

func sortedSquaredArray(array []int) []int {

	lst := make([]int, len(array))

	for i, val := range array {
		lst[i] = val * val

	}

	sort.Ints(lst)

	return lst

}
