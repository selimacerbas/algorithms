def generateDocument(characters, document):

    countedCharacters = set()

    for character in document:

        if character in countedCharacters:
            continue

        documentFrequency = countFrequency(character, document)
        characterFrequency = countFrequency(character, characters)

        if documentFrequency > characterFrequency:
            return False
        
        countedCharacters.add(character)
            
    return True


def countFrequency(targetCharacter, array):
    frequency = 0
    for letter in array:
        if letter == targetCharacter:
            frequency += 1
    
    return frequency
