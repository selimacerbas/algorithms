// This is recursive solution.

package main

import (
	"math"
)

func BinarySearch(array []int, target int) int {
	return binarySearchHelper(array, target, 0, len(array)-1)
}

func binarySearchHelper(array []int, target int, leftPtr int, rightPtr int) int {

	if leftPtr > rightPtr {
		return -1
	}

	midPtr := int(math.Round((float64(leftPtr) + float64(rightPtr)) / 2))
	midElement := array[midPtr]

	if target == midElement {
		return midPtr
	}
	if target <= midElement {
		rightPtr = midPtr - 1
		return binarySearchHelper(array, target, leftPtr, rightPtr)
	} else {
		leftPtr = midPtr + 1
		return binarySearchHelper(array, target, leftPtr, rightPtr)

	}
}
