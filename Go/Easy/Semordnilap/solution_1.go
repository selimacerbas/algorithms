package main

func Semordnilap(words []string) [][]string {

	wordsMap := make(map[string]bool)
	pairs := [][]string{}

	// Add into map
	for _, word := range words {
		wordsMap[word] = true
	}

	for _, word := range words {

		reversedWord := makeReverse(word)

		if _, reverseInSet := wordsMap[reversedWord]; reverseInSet && reversedWord != word {
			pairs = append(pairs, []string{word, reversedWord})
			delete(wordsMap, word)
			delete(wordsMap, reversedWord)
		}
	}

	return pairs
}

func makeReverse(str string) string {

	reversed := []byte{}

	for i := len(str) - 1; i >= 0; i-- {
		reversed = append(reversed, str[i])
	}
	return string(reversed)
}
