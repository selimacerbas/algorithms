package main

import "sort"

func MinimumWaitingTime(queries []int) int {

	hash_tbl := make(map[int]int)
	sort.Ints(queries)
	waitingTime := 0
	totalWaitingTime := 0

	for idx := 0; idx < len(queries)-1; idx++ {

		first := queries[idx]
		second := queries[idx+1]

		waitingTime += first

		hash_tbl[waitingTime] = second

	}

	for key := range hash_tbl {
		totalWaitingTime += key

	}

	return totalWaitingTime

}
