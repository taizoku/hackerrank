#!/bin/python3

import sys

def revisedRussianRoulette(doors):
    # Complete this function

if __name__ == "__main__":
    n = int(input().strip())
    doors = list(map(int, input().strip().split(' ')))
    result = revisedRussianRoulette(doors)
    print (" ".join(map(str, result)))