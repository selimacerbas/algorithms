def insertionSort(array):

    for i in range(1, len(array)):
        j = i

        while j > 0 and array[j] < array[j-1]:
            swap(j, j - 1, array)
            j -= 1
    return array


def swap(index, index_two, array):
    array[index] , array[index_two] = array[index_two] , array[index]