# Drawing Book Example Hackerrank

#!/bin/python3

import os
import sys


def pageCount(n, p):
    n = (n + 1) if n % 2 == 0 else n

    return min(p // 2, (n - p) // 2) # Integer Division

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = int(input())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
