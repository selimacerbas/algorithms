
def selectionSort(array):
   
    for i in range(len(array)):
        k = i
        for j in range(i + 1, len(array)):
            if array[k] > array[j]:
                k = j
        swap(k, i, array)

    return array

def swap(index, indexTwo, array):
    array[index],array[indexTwo] = array[indexTwo] , array[index]