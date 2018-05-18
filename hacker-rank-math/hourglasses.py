    # 0 1 2   1 2 3   2 3 4   3 4 5  

#   0 # 1 1 1   1 1 0   1 0 0   0 0 0
#   1 #   1       0       0       0
#   2 # 1 1 1   1 1 0   1 0 0   0 0 0

#   1 # 0 1 0   1 0 0   0 0 0   0 0 0
#   2 #   1       1       0       0
#   3 # 0 0 2   0 2 4   2 4 4   4 4 0

#   2 # 1 1 1   1 1 0   1 0 0   0 0 0
#   3 #   0       2       4       4
#   4 # 0 0 0   0 0 2   0 2 0   2 0 0

#   3 # 0 0 2   0 2 4   2 4 4   4 4 0
#   4 #   0       0       2       0
#   5 # 0 0 1   0 1 2   1 2 4   2 4 0
import math
import os
import random
import re
import sys
# # Complete the array2D function below.
def array2D(arr):
	max_sum=-999
	for row in range (len(arr)):
		# sum_=0

		for col in range(4):

			if col+2 <len(arr) and row+2<len(arr):

				sum_=arr[row][col]+arr[row][col+1]+arr[row][col+2]
				sum_+=arr[row+1][col+1]
				sum_+=arr[row+2][col]+arr[row+2][col+1]+arr[row+2][col+2]

				max_sum=max(max_sum,sum_)	
	return max_sum		





arr = []

for _ in range(6):
     arr.append(map(int, raw_input().rstrip().split()))

result = array2D(arr)

print result
