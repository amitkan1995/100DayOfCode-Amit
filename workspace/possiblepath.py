# Hackerrank Problem Possible Path

#!/bin/python3

import os
import sys

# Complete the solve function below.
def solve(a, b, x, y):
    if gcd(a,b)==gcd(x,y):
        return "YES"
    else:
        return "NO"

def gcd(a,b):
    x= a if a>b else b
    y= a if a<b else b
    r = b
    while (a%b!=0):
        r=a%b
        a=b
        b=r
    
    return r
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        abxy = input().split()

        a = int(abxy[0])

        b = int(abxy[1])

        x = int(abxy[2])

        y = int(abxy[3])

        result = solve(a, b, x, y)

        fptr.write(result + '\n')

    fptr.close()
