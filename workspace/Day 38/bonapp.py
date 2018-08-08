# Bon Appetit Problem Hackerrank

import math
import os
import random
import re
import sys


if __name__ == '__main__':

    n, k = map(int, input().strip().split(' '))
    bill = [n for n in map(int, input().strip().split(' '))]
    share_charged = int(input())
    share_actual = (sum(bill) - bill[k]) / 2

    if share_actual == share_charged:
        print("Bon Appetit")
    else:
        print(int(share_charged-share_actual))