#!/bin/python3

import sys

def revisedRussianRoulette(doors):
    max = 0
    for door in doors:
        if door == 1:
            max += 1
    return min, max

if __name__ == "__main__":
    n = int(input().strip())
    doors = list(map(int, input().strip().split(' ')))
    result = revisedRussianRoulette(doors)
    print (" ".join(map(str, result)))