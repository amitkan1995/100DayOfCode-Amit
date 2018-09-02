# Equalize Array Hackerrank Problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the equalizeArray function below.
def equalizeArray(arr):
    b = [0]*101
    #print(b)
    m = 0
    for e in arr:
        b[e] += 1
    for e in b:
        m = max(m, e)
    return len(arr)-m

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
