def sortedSquaredArray(array):
    
    lst = [0 for _ in array] #Initialization of array

    for i in range(len(array)):
        val = array[i]
        lst[i] = val * val

    lst.sort()

    return lst
