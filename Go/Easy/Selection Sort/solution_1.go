package main

func SelectionSort(array []int) []int {

	for i := 0; i < len(array); i++ {

		k := i

		for j := i + 1; j < len(array); j++ {

			if array[k] > array[j] {
				k = j
			}
		}
		swap(k, i, array)
	}
	return array
}

func swap(index int, indexTwo int, array []int) {
	array[index], array[indexTwo] = array[indexTwo], array[index]
}
