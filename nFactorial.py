#! usr/bin/env python3

"""
Function to find N Factorial
"""

def nFactorial(n, accumulator):
    N = 1 
    while n>0:
        N = N * n
        n -= accumulator
    return N

def recursiveFactorial(n, accumulator = 1):
    if n == 0:
        return 1
    else:
        return n * recursiveFactorial(n-accumulator, accumulator)

# print(nFactorial(5, 1))
# print(recursiveFactorial(5, 1))
# 
