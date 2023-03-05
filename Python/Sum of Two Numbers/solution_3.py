def twoNumberSum(array, targetSum):

    array.sort()
    first = 0
    second = len(array) - 1

    while first < second:

        currentSum = array[first] + array[second]

        if currentSum == targetSum:
            return [array[first], array[second]]
        elif currentSum < targetSum:
            first += 1
        elif currentSum > targetSum:
            second -= 1

    return []
        
        
