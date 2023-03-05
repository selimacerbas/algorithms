package main

// O(n) time | O(n) space
func TwoNumberSum(array []int, target int) []int {

	numbers := map[int]bool{}

	for _, num := range array {

		match := target - num

		if _, found := numbers[match]; found {

			return []int{match, num}
		}

		numbers[num] = true
	}

	return []int{}
}
