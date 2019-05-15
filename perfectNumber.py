#! usr/bin/env python3

"""
Find the divisorts and perfect number for each int
"""


def divisors(N):
    divisor = []
    for n in range(N+1):
        if n != 0 and not N%n:
            divisor.append(n)
    return divisor

def perfectNumber(N):
    div = divisors(N)
    sumDiv = []
    sumN = 0
    for n in div:
        sumN += n
        if N % sumN:
            sumN -= n
            if sumN not in sumDiv:
                sumDiv.append(sumN)
    return sumDiv

N = 24 
print(f"The perfect number of {N} is {perfectNumber(N)}")

