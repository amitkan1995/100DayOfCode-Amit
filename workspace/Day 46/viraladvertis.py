# Viral Advertising Hackerrank Problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the viralAdvertising function below.
def viralAdvertising(n):
    p = 5
    total_likes = 0
    for i in range(1, n+1):
        likes = p // 2
        total_likes += likes
        p = likes * 3
    return total_likes

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()
