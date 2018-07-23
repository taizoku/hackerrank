# John Watson knows of an operation called a right circular rotation on an array of integers.
# One rotation operation moves the last array element to the first position and shifts all remaining elements right one.
# To test Sherlock's abilities, Watson provides Sherlock with an array of integers.
# Sherlock is to perform the rotation operation a number of times then determine the value of the element at a given position.

# For each array, perform a number of right circular rotations and return the value of the element at a given index.

# EXAMPLE
# - array, a = [3 4 5]
# - number of rotations, k = 2
# - indices to check, m = [1 2]

# First we perform the two rotations:
# [3 4 5] -> [5 3 4] -> [4 5 3]

# Now return the values from the zero-based indices 1 and 2 as indicated in the m array.
# a[1] = 5
# a[2] = 3

# FUNCTION DESCRIPTION
# Complete the circularArrayRotation function in the editor below.
# It should return an array of integers representing the values at the specified indices.

# circularArrayRotation has the following parameter(s):
# - a: an array of integers to rotate
# - k: an integer, the rotation count
# - queries: an array of integers, the indices to report

# INPUT FORMAT
# 1. FIRST line contains THREE SPACE-SEPARATED INTEGERS:
# - n: the number of elements in the integer array
# - k: the rotation count
# - q: the number of queries

# 2. SECOND line contains n SPACE-SEPARATED INTEGERS,
#    where each integer, i describes array element a[i] (where 0 <= i <= n).
#    Each of the q subsequent lines contains a single integer denoting m, the index of the element to return from a.
