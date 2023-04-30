package main

func GenerateDocument(characters string, document string) bool {

	for _, character := range document {

		documentFrequency := countFrequency(character, document)
		characterFrequency := countFrequency(character, characters)

		if documentFrequency > characterFrequency {
			return false
		}
	}

	return true

}

func countFrequency(targetCharacter rune, array string) int {

	var frequency = 0
	for _, char := range array {
		if char == targetCharacter {
			frequency++
		}
	}
	return frequency
}
