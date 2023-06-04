def semordnilap(words):
    wordSet = set(words)
    pairs = []

    for word in words:
        reversedWord = createReverse(word)

        if reversedWord in wordSet:
            pairs.append([word,reversedWord])
            wordSet.remove(word)
            wordSet.remove(reversedWord)

    return pairs
    
    

def createReverse(str):

    reversed = str[::-1]
    
    return reversed

