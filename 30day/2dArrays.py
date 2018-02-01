#!/bin/python3

import sys

arr = []
for arr_i in range(6):
    arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
    arr.append(arr_t)

printer = 0
while printer < 6:
    print(arr[printer])
    printer += 1

down = 0
maxSum = 0

while down < 4:
    across = 0
    while across < 4:
        iterations = 0
        i = down
        print("Down count is:", down)
        j = across
        print("Across count is:", across)

        rowCounter = colCounter = 0
        calculationSum = 0
        while iterations < 7:
            calculationSum += arr[i][j]
            print("rowCounter is now:", rowCounter)
            print("colCounter is now:", colCounter)
            print("Sum is", "arr[", i, "][", j, "] =", calculationSum)
            if calculationSum > maxSum:
                maxSum = calculationSum

            if rowCounter == 0 and colCounter == 2 or rowCounter == 1:
                i += 1
                j -= 1
                rowCounter += 1
                colCounter -= 1

            else:
                j += 1
                colCounter += 1

            iterations += 1
        across += 1
    down += 1
print("Maximum Sum is:", maxSum)
