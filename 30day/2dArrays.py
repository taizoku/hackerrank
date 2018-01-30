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

across = down = 0
rowCounter = colCounter = 1
calculationSum = maxSum = 0

while down < 4:
    i = down

    while across < 4:
        j = across
        iterations = 0

        while iterations < 6:
            calculationSum += arr[i][j]

            print("Sum is", "arr[", i, "][", j, "] =", calculationSum)
            if calculationSum > maxSum:
                maxSum = calculationSum

            if rowCounter % 2 != 0 and colCounter < 4:
                j += 1
                colCounter += 1

            else:
                j -= 1
                i += 1
                rowCounter += 1

            if colCounter == 3:
                rowCounter = 2
                colCounter = 2

            iterations += 1
        across += 1
    down += 1
print("Maximum Sum is:", maxSum)
