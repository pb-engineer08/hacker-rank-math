#!/bin/python3

import math
import os
import random
import re
import sys

    # 0 1 2   1 2 3   2 3 4   3 4 5  

  0 # 1 1 1   1 1 0   1 0 0   0 0 0
  1 #   1       0       0       0
  2 # 1 1 1   1 1 0   1 0 0   0 0 0

  1 # 0 1 0   1 0 0   0 0 0   0 0 0
  2 #   1       1       0       0
  3 # 0 0 2   0 2 4   2 4 4   4 4 0

  2 # 1 1 1   1 1 0   1 0 0   0 0 0
  3 #   0       2       4       4
  4 # 0 0 0   0 0 2   0 2 0   2 0 0

  3 # 0 0 2   0 2 4   2 4 4   4 4 0
  4 #   0       0       2       0
  5 # 0 0 1   0 1 2   1 2 4   2 4 0


# Complete the array2D function below.
def array2D(arr):

    for row in range(6):
        for col in range(6):
            if col==




arr = []

for _ in range(6):
    arr.append(list(map(int, input().rstrip().split())))

result = array2D(arr)

print result
