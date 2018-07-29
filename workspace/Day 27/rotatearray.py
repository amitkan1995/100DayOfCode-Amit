# Array rotation problem from hackerrank

# In python it is like cheating One line solution using slice operator

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    arr = list(map(int, input().rstrip().split()))
    
    for i in range(len(arr)): print(arr[(d%len(arr)+i)%len(arr)],end=" ")
