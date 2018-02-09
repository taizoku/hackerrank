#!/bin/python3

import sys

def revisedRussianRoulette(doors):
    previous_door_locked = False
    min = max = 0
    for door in doors:
        if door == 0:
            if previous_door_locked is True:
                min += 1 # bug for 1 at end
                previous_door_locked = False

        if door == 1:
            if previous_door_locked is True:
                min += 1
                previous_door_locked = False

            else:
                previous_door_locked = True
            max += 1
    return min, max

if __name__ == "__main__":
    n = int(input().strip())
    doors = list(map(int, input().strip().split(' ')))
    result = revisedRussianRoulette(doors)
    print (" ".join(map(str, result)))