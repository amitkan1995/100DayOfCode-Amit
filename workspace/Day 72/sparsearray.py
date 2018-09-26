# Sparse Array Hackerrank Problem
# Its on Python 2
#!/bin/python

import math
import os
import random
import re
import sys

# Complete the matchingStrings function below.
def matchingStrings(strings, queries):
    counts=[]
    for i in queries:
        counts.append(strings.count(i))
    return counts

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    strings_count = int(raw_input())

    strings = []

    for _ in xrange(strings_count):
        strings_item = raw_input()
        strings.append(strings_item)

    queries_count = int(raw_input())

    queries = []

    for _ in xrange(queries_count):
        queries_item = raw_input()
        queries.append(queries_item)

    res = matchingStrings(strings, queries)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
