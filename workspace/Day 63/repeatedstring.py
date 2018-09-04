# Repeated String Hackerrank Problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    ans  = 0
    for i in s :
        if i == 'a':
            ans += 1
    k = n//len(s)
    ans *= k
    r = n%len(s);
    for i in range(0,r):
        if s[i] == 'a':
            ans += 1
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
