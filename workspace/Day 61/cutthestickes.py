# Cut The Stickes Problem from Hackerrank

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the cutTheSticks function below.
def cutTheSticks(arr):
    N=len(arr)
    A=sorted(list(set(arr)))
    answer=[]
    count=N
    for a in A:
        answer.append(count)
        count-=arr.count(a)
    return answer

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
