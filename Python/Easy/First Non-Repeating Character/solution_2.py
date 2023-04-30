def firstNonRepeatingCharacter(string):

    frequency = {}

    for element in string:
        frequency[element] = frequency.get(element, 0) + 1

    for index in range(len(string)):
        letter = string[index]
        if frequency[letter] == 1:
            return index
            
    return -1
