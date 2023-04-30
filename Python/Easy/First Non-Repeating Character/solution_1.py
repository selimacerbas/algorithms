def firstNonRepeatingCharacter(string):

    for first in range(len(string)):
        found = False
        for second in range(len(string)):

            if first != second and string[first] == string[second]:
                found = True
                
        if not found:
            return first
    
    return -1
