# Pick Numbers Problem from Hackerrank

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the pickingNumbers function below.
def pickingNumbers(a):
    answer = 0
    # Unique list, so iteration will be less.
    ua = set(a)
    for value in ua:
        c = a.count(value)
        d = a.count(value+1)
        c = c + d
        if c > answer:
            answer = c
            
    return answer

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
