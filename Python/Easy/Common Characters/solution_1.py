def commonCharacters(strings):

    charCounts = {}
    finalCount = []

    for string in strings:
        setOfString = set(string)

        for element in setOfString:

            if element not in charCounts:
                charCounts[element] = 0
            if element in charCounts:
                charCounts[element] += 1

    for character, count in charCounts.items():
         if count == len(strings):
            finalCount.append(character)
    return finalCount
