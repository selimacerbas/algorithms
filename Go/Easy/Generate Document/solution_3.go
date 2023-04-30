package main

func GenerateDocument(characters string, document string) bool {

	characterCounts := map[rune]int{}

	for _, character := range characters {
		characterCounts[character] = characterCounts[character] + 1
	}

	for _, character := range document {
		if characterCounts[character] == 0 {
			return false
		}

		characterCounts[character] = characterCounts[character] - 1
	}

	return true

}
