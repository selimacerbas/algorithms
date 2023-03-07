package main

func IsValidSubsequence(array []int, sequence []int) bool {

	index1 := 0
	index2 := 0

	for index1 < len(array) && index2 < len(sequence) {

		if array[index1] == sequence[index2] {
			index2++
		}
		index1++
	}
	return index2 == len(sequence)
}
