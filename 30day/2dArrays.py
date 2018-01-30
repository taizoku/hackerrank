#!/bin/python3

import sys


arr = []
for arr_i in range(6):
   arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
   arr.append(arr_t)

j = 0
while j < 6:
    print(arr[j])
    j += 1

j = 0
rowCounter = colCounter = 1
calculationSum = maxSum = 0

read = input()
if read == exit:
    sys.exit

for rows in arr:
    calculationSum += rows[j]

    print("sum is", calculationSum)
    if calculationSum > maxSum:
        maxSum = calculationSum

    #for 3
    if colCounter < 4:
        calculationSum = 0

        if rowCounter % 2 != 0 and colCounter % 2 != 0: # if counter is not even
            j += 1

        else:
            j = 1

    colCounter += 1
