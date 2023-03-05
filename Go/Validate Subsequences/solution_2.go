package main

func IsValidSubsequence(array []int, sequence []int) bool {

	var index int

	for _, val := range array {

		if index == len(sequence) {
			break
		}

		if val == sequence[index] {
			index++
		}
	}

	return index == len(sequence)

}
