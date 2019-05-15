#! usr/bin/env python3

"""
Algorithm to perform checksum on ISBN numbers. 
"""


def ISBN(num):
    """
    Perform checksum on ISBN

    Returns
    -------
    0-9 or X if sum >= 10
    """
    checkSum = []
    # Stringify num
    for index, digit in enumerate(num):
        checkSum.append((index + 1) * int(digit))
    checkSum = sum(checkSum) % 11
    if checkSum >=10:
        return 'X'
    return checkSum

newISBN = '019281022'
checkSum = ISBN(newISBN)

print(f"The full ISBN is: {newISBN}{checkSum}")

