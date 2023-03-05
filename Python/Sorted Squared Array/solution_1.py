def sortedSquaredArray(array):
    
    lst = []

    for val in array:
        lst.append(val**2)
        
    lst.sort()
    
    return lst
