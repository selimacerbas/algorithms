def generateDocument(characters, document):

    for character in document:

        documentFrequency = countFrequency(character, document)
        characterFrequency = countFrequency(character, characters)

        if documentFrequency > characterFrequency:
            return False
            
    return True


def countFrequency(targetCharacter, array):
    frequency = 0
    for letter in array:
        if letter == targetCharacter:
            frequency += 1
    
    return frequency
