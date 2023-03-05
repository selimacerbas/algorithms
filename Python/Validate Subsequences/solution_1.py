# O(N) Time | O(1) Space 
def isValidSubsequence(array, sequence) -> bool:

    index1 = 0
    index2 = 0

    while index1 < len(array) and index2 < len(sequence):

        if array[index1] == sequence[index2]:
            index2 += 1
        index1 += 1
    
    return index2 == len(sequence)
    
        