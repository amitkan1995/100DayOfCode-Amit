# Hackerrank Divisible Sum Pairs 


import math
import os
import random
import re
import sys
from itertools import combinations

# Running time O(n^2)
def divisibleSumPairs(n, k, ar):
    pairs = [sum(pair) % k for pair in combinations(ar, 2)]
    return pairs.count(0)
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
