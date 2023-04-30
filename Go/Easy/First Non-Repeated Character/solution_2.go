package main

// O(n) time / O(1) space since only 26 letters it can be
func FirstNonRepeatingCharacter(str string) int {

	frequency := make(map[rune]int)

	for _, letter := range str {
		frequency[letter] = frequency[letter] + 1
	}

	for index, letter := range str {
		if frequency[letter] == 1 {
			return index
		}
	}

	return -1
}
