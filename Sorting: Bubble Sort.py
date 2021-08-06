# Sorting: Bubble Sort

# HackerRank Problem Solved using Python.

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    # Write your code here
    swap = 0

    for i in range(n):
        cs = 0

        for j in range(0,n-1):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
                cs+=1
                
        swap += cs
                
        if cs == 0:
            break
        
    print("Array is sorted in " + str(swap) + " swaps.")
    print("First Element: " + str(a[0]))
    print("Last Element: " + str(a[-1]))
        

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
