def sortedSquaredArray(array):
    
    lst = [0 for _ in array] #Initialization of array

    left_index = 0
    right_index = len(array) - 1

    for i in reversed(range(len(array))):
        left_val = array[left_index]
        right_val = array[right_index]

        if abs(left_val) > abs(right_val):
            lst[i] = left_val**2
            left_index += 1
        else:
            lst[i] = right_val**2
            right_index -= 1

    return lst
