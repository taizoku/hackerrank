#!/bin/python3

import sys


arr = []
for arr_i in range(6):
   arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
   arr.append(arr_t)

i = j = 0
col = counter = 1
calculationSum = maxSum = 0
for numbers in arr:
    calculationSum += arr[i][j]
    if counter % 2 != 0: # if counter is not even
        i += 2
        counter = 0

    else:
        j += 1

    counter += 1