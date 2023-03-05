
# O(N) | O(1)
def isValidSubsequence(array, sequence) -> bool:

    index = 0

    for element in array:

        if index == len(sequence):
            break

        if sequence[index] == element:
            index += 1
    
    return index == len(sequence)
    
        