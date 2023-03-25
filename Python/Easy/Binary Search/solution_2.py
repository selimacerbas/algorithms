import math

#While loop
def binarySearch(array, target):
    return binarySearchHelper(array, target, 0, len(array) - 1)

def binarySearchHelper(array, target , leftPtr, rightPtr):
   
    while leftPtr <= rightPtr:
        midPtr = math.floor((rightPtr + leftPtr) / 2)
        midElement = array[midPtr]
        if target == midElement:
            return array.index(midElement)
        elif target < midElement:
            rightPtr = midPtr - 1
        else:
            leftPtr = midPtr + 1
    
    return -1


    
