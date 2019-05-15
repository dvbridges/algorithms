#! usr/bin/env python3

from nFactorial import nFactorial


# Create pascal trial

rows = 8 
entries = sum(list(range(1,9)))

def createBaseTriangle(rows, item):
    """
    Creates base Pascals Triangle, consisting of 1's
    """
    T = []
    for row in range(rows):
        temp = []
        for n in range(item):
            temp.append(1)
        T.append(temp)
        item += 1
    return T


# Start algorithms
# Simple "add two numbers above to get current value" algorithm

T = createBaseTriangle(rows, 1)
for index in range(len(T)):
    if index > 1:
        for i in range(len(T[index])):
            try:
                previousRow = T[index-1]
                assert((i-1) != -1)
                left = previousRow[i-1]
                right = previousRow[i]
                T[index][i] = left + right
            except IndexError as err:
                print(err)
            except AssertionError as err:
                print("Index Error - left number < 0")
print(T)

# 

T = createBaseTriangle(rows, 1)

for index in range(len(T)):
    if index > 1:
        for i in range(len(T[index])):
            try:
                assert((i-1) != -1)
                T[index][i] = nFactorial(index, 1)/(nFactorial(i, 1)*nFactorial(index-i, 1))
            except IndexError as err:
                print(err)
            except AssertionError as err:
                print("Index Error - left number < 0")

print(T)
