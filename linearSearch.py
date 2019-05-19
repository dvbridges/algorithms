#! usr/bin/env

def linearSearch(array, searchVal):

    for element in array:
        if searchVal == element:
            return True
    return False

array = [1,2,3,4,6,7,8,9]
print(linearSearch(array, 5))
print(linearSearch(array, 6))

