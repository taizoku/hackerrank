# Link: https://www.hackerrank.com/challenges/non-divisible-subset/problem

# PROBLEM
# Given a set of distinct integers, print the size of the maximal subset of S,
# where the sum of any 2 numbers in S' is not evenly divisible by k

# EXAMPLE
# Given the array S = [19, 10, 12, 10, 24, 25, 22] and k = 4
# - One array that can be created is S'[0] = [10, 12, 25]
# - Another is S'[1] = [19, 22, 24]
# - From these, the max length solution array has 3 elements

# SOLUTION
# The algorithm that solves this is as follows:
# Given the integer k, we must ensure that the sum of any pair does not divide evenly
# - This hints that we are dealing with REMAINDERS (or modulo)
# - For a given k, there is a pair of REMAINDERS that tells us what we should avoid
# - This is such that a complementary pair of remainders added together make an evenly divisible number
#
# * Therefore, we need to AVOID numbers in a subset where (A % K) + (B % K) == K
# * This ALSO includes the edge case where (A % K) == (B % K) == 0
# * This means that if we ever have a subset where any number is evenly divisible, you cannot have another
# * In ADDITION, we can only have one value in a subset where (A % K) == (B % K)

# FUNCTION DESCRIPTION
# Has the following parameters:
# - S: an array of integers
# - k: an integer


def nonDivisibleSet(s, k):
    avoid = {}
    for i in range(1, k):
        avoid[i] = k-i
    print(avoid)

    subset = []
    # if k is 4 then we have to avoid [1, 3], [2, 2]
    for i in s:
        if i not in subset:
            subset.append(i % k)

    print(subset)

    return 1  # length of longest subset


numValues, nonFactor = map(int, input().split(' '))
uniqueSet = list(map(int, input().split(' ')))
nonDivisibleSet(uniqueSet, nonFactor)
