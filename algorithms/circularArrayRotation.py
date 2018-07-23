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
