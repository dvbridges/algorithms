from insertionSort import insertionSort
import timeit

SETUP_CODE = """
from random import sample
from __main__ import insertionSort

# Create random array for timing
array = sample(range(0, 1000), 1000)
"""
TEST_CODE = """
insertionSort(array)
"""
N = 10000
times = timeit.timeit(setup=SETUP_CODE, stmt=TEST_CODE, number=N)
print("{} usec/pass".format(times/N))

