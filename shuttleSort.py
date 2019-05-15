#! usr/bin/env python3

def shuttleSort(array):
    """
    Shuttle sort algorithm 
    Bit like a reverse bubble sort
    Higher numbers sink to the bottom
    """
    for i in range(1, len(array)):
        for j in range(i, 0, -1):
            if array[j-1] > array[j]: 
               temp = array[j-1]
               array[j-1] = array[j]
               array[j] = temp
    return array

unsorted = list(range(11))
unsorted.sort(reverse=True)
print(unsorted)
print(shuttleSort(unsorted))
