package main

import "sort"

func ClassPhotos(redShirtHeights []int, blueShirtHeights []int) bool {

	sort.Ints(redShirtHeights)
	sort.Ints(blueShirtHeights)

	var firstLineColor string

	if redShirtHeights[0] > blueShirtHeights[0] {

		firstLineColor = "RED"

	} else {

		firstLineColor = "BLUE"
	}

	if firstLineColor == "RED" {

		for idx, heightOfRed := range redShirtHeights {
			heightOfBlue := blueShirtHeights[idx]

			if heightOfRed <= heightOfBlue {
				return false

			}
		}
	}

	if firstLineColor == "BLUE" {

		for idx, heightOfBlue := range blueShirtHeights {
			heightOfRed := redShirtHeights[idx]

			if heightOfBlue <= heightOfRed {
				return false

			}
		}
	}

	return true

}
