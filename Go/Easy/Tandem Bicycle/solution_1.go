package main

import (
	"math"
	"sort"
)

func TandemBicycle(redShirtSpeeds []int, blueShirtSpeeds []int, fastest bool) int {

	var sumOfSpeeds int = 0
	sort.Ints(redShirtSpeeds)

	if fastest == true {
		sort.Ints(blueShirtSpeeds)

		for idx, _ := range redShirtSpeeds {

			riderRed := redShirtSpeeds[len(redShirtSpeeds)-(idx+1)]
			riderBlue := blueShirtSpeeds[idx]

			maxPairedSpeed := int(math.Max(float64(riderRed), float64(riderBlue)))

			sumOfSpeeds += maxPairedSpeed

		}
	}

	if fastest == false {
		sort.Sort(sort.Reverse(sort.IntSlice(blueShirtSpeeds)))

		for idx, _ := range redShirtSpeeds {

			riderRed := redShirtSpeeds[len(redShirtSpeeds)-(idx+1)]
			riderBlue := blueShirtSpeeds[idx]

			maxPairedSpeed := int(math.Max(float64(riderRed), float64(riderBlue)))

			sumOfSpeeds += maxPairedSpeed

		}

	}

	return sumOfSpeeds

}
