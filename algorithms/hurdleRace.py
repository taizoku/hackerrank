# Dan is playing a video game in which his character competes in a hurdle race.
# Hurdles are of varying heights, and Dan has a maximum height he can jump.
# There is a magic potion he can take that will increase his maximum height by  unit for each dose.
# How many doses of the potion must he take to be able to jump all of the hurdles?

# Given an array of hurdle heights "height", and an initial maximum height Dan can jump, k,
# determine the minimum number of doses Dan must take to be able to clear all the hurdles in the race.

# eg eight 1 2 3 3 2 dan can jump 1 unit high naturally
# he must take 3-1=2 doses of potion to be able to jump all of the hurdles

# first line two integers n and k
numHurdles, maxJump = map(int, input().strip().split(' '))

# eg
# 5 4
# 1 6 3 5 2
# sample output 2