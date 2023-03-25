def bubbleSort(array):

    sorted = False
    while not sorted:
        sorted = True
        for idx in range(len(array) - 1):
            if array[idx] > array[idx + 1]:
                array[idx] , array[idx + 1] = array[idx + 1] , array[idx]
                sorted = False
                

    return array