#!/bin/python3

import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

string = ""
for i in range(n):
    string += str(arr[n-1])
    if n != 0:
        string += " "
    n -= 1
print(string)