#Hard Coded
def findThreeLargestNumbers(array) -> list:

    lst = [None,None,None]

    for element in array:

        if lst[2] == None or element > lst[2]:
            lst[0] = lst[1]
            lst[1] = lst[2]
            lst[2] = element
        elif lst[1] == None or element > lst[1]:
            lst[0] = lst[1]
            lst[1] = element
        elif lst[0] == None or element > lst[0]:
            lst[0] = element
        
    return lst
