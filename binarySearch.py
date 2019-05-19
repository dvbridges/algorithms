#! usr/bin/env python3

def binarySearch(array, searchVal):
    """
    Binary Search
    Assumes sorted array
    """
    # Get middle value
    found = False
    while not found and len(array) >= 1:
        midPoint = len(array)//2
        if searchVal == array[midPoint]:
            found = True
        elif searchVal < array[midPoint]:
            array = array[0:midPoint]
        else:
            array = array[midPoint+1:]
    if found:
        return True
    return False

array = [1,2,3,4,5]
print(binarySearch(array, 5))
print(binarySearch(array, 6))
print(binarySearch(array, 1))


