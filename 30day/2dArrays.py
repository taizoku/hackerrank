#!/bin/python3

import sys


# Just prints the input array to stdout
def print_array():
    printer = 0
    while printer < 6:
        print(arr[printer])
        printer += 1


arr = []
for arr_i in range(6):
    arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
    arr.append(arr_t)

# print_array()

down = 0
calculationSum = maxSum = 0

while down < 4:
    across = 0
    while across < 4:
        maxSum = max(maxSum, calculationSum)
        iterations = 0
        x = down
        # print("Down count is:", down)
        y = across
        # print("Across count is:", across)

        rowCounter = colCounter = 0
        calculationSum = 0
        while iterations < 7:
            calculationSum += arr[x][y]
            '''
            print("rowCounter is now:", rowCounter)
            print("colCounter is now:", colCounter)
            print("Sum is", "arr[", x, "][", y, "] =", calculationSum)
            '''
            if (rowCounter == 0 and colCounter == 2) or (rowCounter == 1):
                x += 1
                y -= 1
                rowCounter += 1
                colCounter -= 1

            else:
                y += 1
                colCounter += 1

            iterations += 1
        across += 1
    down += 1
# print("Maximum Sum is:", maxSum)
print(maxSum)
