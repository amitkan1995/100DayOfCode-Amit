# Between Two Sets Problem from Hackerrank

#!/bin/python3

import os
import sys

#Complete the getTotalX function in the editor below. It should return the number of integers that are betwen the sets.

#getTotalX has the following parameter(s):

#    a: an array of integers
#    b: an array of integers



def getTotalX(a, b):
    nmax,nmin,count = max(a),min(b),0
    for i in range(1,int(nmin/nmax)+1):
        if(sum((i*nmax)%n for n in a)+sum(n%(i*nmax) for n in b))==0:
            count+=1
    return count
    

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    total = getTotalX(a, b)

    f.write(str(total) + '\n')

    f.close()
