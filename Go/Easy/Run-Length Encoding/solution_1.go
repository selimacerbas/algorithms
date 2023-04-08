package main

import "strconv"

func RunLengthEncoding(str string) string {

	left := 0
	right := 0
	counter := 0
	charLst := []byte{}

	for right < len(str) {

		mainChar := str[left]
		walkingChar := str[right]

		if (mainChar == walkingChar) && (counter != 9) {

			right += 1
			counter += 1

			//Handle last run
			if right == len(str) {
				addChar(counter, mainChar, &charLst)
			}
		} else {

			addChar(counter, mainChar, &charLst)

			left = right
			counter = 0
		}
	}
	return string(charLst)

}

func addChar(number int, char byte, char_lst *[]byte) {

	*char_lst = append(*char_lst, strconv.Itoa(number)[0])
	*char_lst = append(*char_lst, char)
}
