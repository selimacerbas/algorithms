package main

func IsPalindrome(str string) bool {

	left := 0
	right := len(str) - 1
	isFound := false

	for left <= right {

		if str[left] == str[right] {
			isFound = true
			left += 1
			right -= 1
		} else {
			isFound = false
			return isFound
		}
	}

	return isFound
}
