# LeaderBoard Hackerrank Problem

import math
import os
import random
import re
import sys

# Complete the climbingLeaderboard function below.
def climbingLeaderboard(scores, alice):
    a = sorted(list(set(scores)))
    mes=len(a)
    b = []
    for el in alice:
        while mes>0:
            if el>a[0]:
                a.remove(a[0])
                mes-=1
                continue
            elif el==a[0]:
                b.append(mes)
                break
            else:
                b.append(mes+1)
                break
        if mes==0:
            b.append(1)
    return b

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    scores_count = int(input())

    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(scores, alice)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
