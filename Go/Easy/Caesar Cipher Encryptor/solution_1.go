package main

import "strings"

func CaesarCipherEncryptor(str string, key int) string {

	alphabet := "abcdefghijklmnopqrstuvwxyz"
	var lst []rune
	input_idx := 0

	for input_idx < len(str) {

		firstLetter := rune(str[input_idx])
		//Abstraction
		newLetter := findAndShift(firstLetter, key, alphabet)
		lst = append(lst, newLetter)
		input_idx += 1

	}

	return string(lst)
}

func findAndShift(letter rune, shift int, alphabet string) rune {

	newLetterCode := (strings.Index(alphabet, string(letter)) + shift) % 26
	newLetter := alphabet[newLetterCode]
	return rune(newLetter)

}
