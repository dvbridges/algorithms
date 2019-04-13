#!/usr/bin/env/ python

"""
The insertion sort algorithm
"""

def insertionSort(array):
    for element in range(1, len(array)):
        key = array[element]
        i = element - 1
        while i >= 0 and array[i] > key:
            array[i+1] = array[i]
            i -= 1
        array[i+1] = key
    return array

