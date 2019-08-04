#PROBLEM
# A left rotation operation on an array shifts each of the array's elements  unit to the left.
# For example, if  left rotations are performed on array , then the array would become .

# Given:
# - an array a of n integers
# - and a number, d
# perform d left rotations on the array.
# Return the updated array to be printed as a single line of space-separated integers.

import os


# Complete the rotLeft function below.
def rotLeft(a, d):
    b = list(a)
    for i in range(len(a)):
        b[i-d] = a[i]  # b is considering each element in a and shifting to position -d
    return b


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
