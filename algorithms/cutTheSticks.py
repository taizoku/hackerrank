# Link: https://www.hackerrank.com/challenges/cut-the-sticks/problem

# PROBLEM
# You are given a number of sticks of varying lengths. You will iteratively cut the sticks into smaller sticks,
# discarding the shortest pieces until there are none left. At each iteration you will determine the length of
# the shortest stick remaining, cut that length from each of the longer sticks and then discard all the pieces
# of that shortest length. When all the remaining sticks are the same length, they cannot be shortened so discard them.

# Given the:
# - lengths of 'n' sticks
# print the number of sticks that are left before each iteration until there are none left.

# EXAMPLE
# There are 'n = 3' sticks of lengths arr = [1, 2, 3].
# The shortest stick length is 1
# -> so we cut that length from the longer two and discard the pieces of length 1.

# Now our lengths are arr = [1, 2].
# Again, the shortest stick is of length 1
# -> so we cut that amount from the longer stick and discard those pieces.
# There is only one stick left, arr = [1], so we discard that stick.
# Our lengths are [3, 2, 1].


# FUNCTION
def cutTheSticks(array):
    # initialisation
    modifiedArray = array
    firstSpace = ' '*(len(array))

    while array is not []:
        removedCut = sorted(array)[0]
        # for each operation, print
        print('sticks-length' + firstSpace, 'length-of-cut', firstSpace + 'sticks-cut')

        sticksLeft = len(modifiedArray)

        print(array, firstSpace, removedCut, firstSpace*2 + 4*' ', sticksLeft)

    return 0


# INPUT
sizeOfArray = int(input())

array = list(map(int, input().strip().split(' ')))

# OUTPUT
cutTheSticks(array)
