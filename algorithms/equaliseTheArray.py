# Link: https://www.hackerrank.com/challenges/equality-in-a-array/problem

# PROBLEM
# Karl has an array of integers.
# He wants to reduce the array until all remaining elements are equal.
# Determine the minimum number of elements to delete to reach his goal.

# EXAMPLE
# If his array is arr = [1, 2, 2, 3], we see that he can delete the 2 elements 1 and 3 leaving arr = [2, 2].
# He could also delete both twos and either the 1 or the 3, but that would take 3 deletions.
# The minimum number of deletions is 2.

# FUNCTION DESCRIPTION
# equalizeArray() must return an integer that denotes the minimum number of deletions required.
# It also has the following parameter(s):
# - arr: an array of integers

# INPUT FORMAT
# 1. The first line contains an integer n, the number of elements in arr.
# 2. The next line contains n space-separated integers arr[i].

# OUTPUT FORMAT
# Print the minimum number of elements Karl must delete for all elements in the array to be equal.

import operator


def equalizeArray(arr):
    count = {}
    for i in arr:
        if i not in count:
            count[i] = 1
        else:
            count[i] = count[i] + 1

    highest = max(count.items(), key=operator.itemgetter(1))[0]
    return len(arr) - count[highest]


numElements = int(input())
array = list(map(int, input().split(' ')))
print(equalizeArray(array))
