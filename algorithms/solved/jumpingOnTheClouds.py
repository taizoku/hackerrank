# Link: https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem

# PROBLEM
# Emma is playing a new mobile game that starts with consecutively numbered clouds.
# - Some of the clouds are thunderheads and others are cumulus.
# - She can jump on any cumulus cloud having a number that is equal to the number of the current cloud plus 1 or 2.
# - She must avoid the thunderheads.
#
# Determine the minimum number of jumps it will take Emma to jump from her starting postion to the last cloud.
# It is always possible to win the game.

# EXAMPLE
# Emma will get an array of clouds numbered:
# - 0: if they are safe
# - 1: if they must be avoided.
#
# Take c = [0, 1, 0, 0, 0, 1, 0], indexed from 0 to 6.
# The number on each cloud is its index in the list so she must avoid the clouds at indexes 1 and 5.
# She could follow the following two paths:
# 1: 0 -> 2 -> 4 -> 6
# 2: 0 -> 2 -> 3 -> 4 -> 6
# The first path takes 3 jumps while the second takes 4.

# FUNCTION DESCRIPTION
# jumpingOnClouds() should return the minimum number of jumps required, as an integer.
# It also has the following parameters:
# - c: an array of binary integers

# INPUT FORMAT
# 1. The first line contains an integer n, the total number of clouds.
# 2. The second line contains n space-separated binary integers describing clouds c[i].

# OUTPUT FORMAT
# Print the minimum number of jumps needed to win the game.


def jumpingOnClouds(n, c):
    i = jumps = 0  # i keeps track of the position
    # jumps counts the number of jumps taken

    while i < n-1:  # while position not at the end of the list
        if i + 2 < n:  # make sure we don't overextend the bounds
            if c[i + 2] != 1:  # check to see if jumping two spaces is safe (best)
                i += 2
            else:  # otherwise we have to move once
                i += 1
        else:  # if not, we can only move one
            i += 1
        jumps += 1
    return jumps


print(jumpingOnClouds(7, [0, 1, 0, 0, 0, 1, 0]))
print()
print(jumpingOnClouds(7, [0, 0, 1, 0, 0, 1, 0]))
print()
print(jumpingOnClouds(6, [0, 0, 0, 0, 1, 0]))
# numClouds = int(input())
# clouds = list(map(int, input().split(' ')))
# print(jumpingOnClouds(numClouds, clouds))
