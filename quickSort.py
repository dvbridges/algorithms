#! usr/bin/env python3

from numpy.random import shuffle

def swap(array, p1, p2):
    temp = array[p1]
    array[p1] = array[p2]
    array[p2] = temp

def quickSort(array, first, last):
    if first < last:
        splitPoint = partition(array, first, last)

        quickSort(array, first, splitPoint-1)
        quickSort(array, splitPoint+1, last)
    return array

def partition(array, first, last):
    
    pivotValue = array[first]

    leftPos = first + 1
    rightPos = last
    
    done = False

    while not done:
        while leftPos <= rightPos and array[leftPos] <= pivotValue: 
            leftPos += 1
        while array[rightPos] >= pivotValue and rightPos >= leftPos:
            rightPos -= 1
        if rightPos < leftPos:
            done = True
        else:
            swap(array, leftPos, rightPos)
    swap(array, first, rightPos)
    return rightPos



# Create array
for i in range(10):
    array = [1,2,3,4,5,6,7,8,9]
    shuffle(array)
    print(quickSort(array, 0, len(array)-1))





