package main

func InsertionSort(array []int) []int {

	for i := 1; i < len(array); i++ {

		j := i

		for j >= 0 && array[j] < array[j-1] {
			swap(j, j-1, array)
			j -= 1

		}
	}

	return array
}

func swap(index int, indexTwo int, array []int) {
	array[index], array[indexTwo] = array[indexTwo], array[index]
}
