package main

// O(n^2) time | O(1) space
func TwoNumberSum(array []int, target int) []int {

	var lst []int

	for i := 0; i < len(array); i++ {
		for j := i + 1; j < len(array); j++ {

			first := array[i]
			second := array[j]

			if first+second == target {
				append(lst, first)
				append(lst, second)
				return lst
			}
		}
	}
	return lst
}
