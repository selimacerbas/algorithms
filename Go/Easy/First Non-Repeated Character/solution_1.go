package main

func FirstNonRepeatingCharacter(str string) int {

	for first := range str {

		found := false

		for second := range str {

			if (first != second) && (str[first] == str[second]) {
				found = true
			}
		}

		if !found {
			return first
		}

	}

	return -1
}
