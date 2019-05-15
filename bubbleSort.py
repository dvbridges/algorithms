#! usr/bin/env python3

def bubbleSort(array):
    """
    Bubble sort algorithm:
    Sum of n-1 where n = list.
    Max number of swaps per pass == n-1
    """
    for i in range(0, len(array)-1):
        for j in range(0, len(array)-i):
            if array[j+1] > array[j]: 
               temp = array[j+1]
               array[j+1] = array[j]
               array[j+1] = temp
    return array

unsorted = list(range(11))
unsorted.sort(reverse=True)
print(unsorted)
print(bubbleSort(unsorted))
