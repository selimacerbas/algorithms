package main

func BubbleSort(array []int) []int {

	sorted := false
	counter := 0

	for !sorted {

		sorted = true

		for i := 0; i < len(array)-1-counter; i++ {

			if array[i] > array[i+1] {
				array[i], array[i+1] = array[i+1], array[i]
				sorted = false
			}
		}
		counter++
	}
	return array
}
