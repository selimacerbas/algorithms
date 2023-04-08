def runLengthEncoding(string):

    left = 0
    right = 0
    counter = 0
    charLst = []


    while right < len(string):

        mainChar = string[left]
        walkingChar = string[right]

        if mainChar is walkingChar and counter is not 9:
            right += 1
            counter += 1
            
            #Handle last run
            if right == len(string):
                addChar(counter, mainChar, charLst)
                
        else:
            addChar(counter, mainChar, charLst)
            left = right
            counter = 0

    return "".join(charLst)

def addChar(number, char, array):
    array.append(str(number))
    array.append(char)
    
    