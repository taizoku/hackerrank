#!/bin/python3

import sys


def simple_array_sum(n, ar):
    result = 0
    while n != 0:
        result += ar[n-1]
        n -= 1
    return result


n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = simple_array_sum(n, ar)
print(result)