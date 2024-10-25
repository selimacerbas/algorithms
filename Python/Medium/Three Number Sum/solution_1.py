from typing import List

def threeNumberSum(array : List, targetSum : int):
    sorted_array = sorted(array)
    triplets = []
    for i in range(len(sorted_array) - 2):
        left = i + 1
        right = len(array) - 1
        while left < right:
            currentSum = sorted_array[i] + sorted_array[left] + sorted_array[right]
            if currentSum == targetSum:
                triplets.append([sorted_array[i] , sorted_array[left] , sorted_array[right]])
                left += 1
                right -= 1
            elif currentSum < targetSum:
                left += 1
            elif currentSum > targetSum:
                right -= 1



