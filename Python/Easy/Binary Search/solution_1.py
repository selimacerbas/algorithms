import math

#This is a recursive approach.
def binarySearch(array, target):
    return binarySearchHelper(array, target, 0, len(array) - 1)

def binarySearchHelper(array, target , leftPtr, rightPtr):
    midPtr = math.floor((rightPtr + leftPtr) / 2)
    midElement = array[midPtr]
    
    if leftPtr > rightPtr:
        return -1
    elif target == midElement:
        return array.index(midElement)
    elif target < midElement:
        rightPtr = midPtr - 1
        return binarySearchHelper(array, target, leftPtr, rightPtr)
    else:
        leftPtr = midPtr + 1
        return binarySearchHelper(array, target , leftPtr , rightPtr)


    
