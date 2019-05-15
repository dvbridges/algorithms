#! usr/bin/env python3

def selectionSort(array):
    """
    Selection/ interchange sort algorithm:
    Sum of n-1 where n = list.
    Max number of swaps per pass == n-1
    """
    for i in range(0, len(array)-1):
        for j in range(i, len(array)):
            if array[j] < array[i]:
               temp = array[i]
               array[i] = array[j]
               array[j] = temp
    return array

unsorted = list(range(11))
unsorted.sort(reverse=True)
print(unsorted)
print(selectionSort(unsorted))
               

            



