# Find Digits problem from Hackerrank

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the findDigits function below.
def findDigits(n):
    x=str(n)
    a=0
    for i in x:
        i=int(i)
        if i!=0:
            if n%i==0:
                a+=1
        else:
            continue
    return(a)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = findDigits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
