def commonCharacters(strings):

    smallest = findSmallestString(strings)
    potential = set(smallest)

    for string in strings:
        removeUnnecessary(string, potential)
    return list(potential)



def findSmallestString(strings):
    smallest = strings[0]
    
    for string in strings:
        if len(string) < len(smallest):
            smallest = string
            
    return smallest

def removeUnnecessary(string, potential):
    unique = set(string)

    for element in list(potential):
        if element not in unique:
            potential.remove(element)
            