# Migratory Birds Hackerrank


import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
def migratoryBirds(ar):
    n = len(ar)
    counter_ar = [0]*(n+1)
    for value in ar:
        counter_ar[value] += 1
    m = max(counter_ar)
    result = 0
    for i in range(len(counter_ar)):
        if counter_ar[i] == m:
            result = i
            break
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
