# SOLVED: ryotokuro 26/08/18
# LINK (HackerRank): https://www.hackerrank.com/challenges/find-digits/problem

# BACKGROUND
# An integer d is a divisor of an integer n if the remainder of n / d = 0.

# PROBLEM
# Given an integer, for each digit that makes up the integer determine whether it is a divisor.
# Count the number of divisors occurring within the integer.

# NOTE
# Each digit is considered to be unique, so each occurrence of the same digit should be counted
# (e.g. for n = 111, 1 is a divisor of 111 each time it occurs so the answer is 3).


# FUNCTION DESCRIPTION
# It should return an integer representing the number of digits of d that are divisors of d.
# findDigits has the following parameter(s):
#   - n: an integer to analyze
def findDigits(integer):
    numDivisors = 0
    digit = str(integer)
    for i in range(len(digit)):
        potentialDivisor = int(digit[i])
        print('digit: ', potentialDivisor)
        if potentialDivisor != 0:
            # if n / d == 0
            if integer % potentialDivisor == 0:
                numDivisors += 1  # then it is a divisor
    return numDivisors


# INPUT FORMAT
# The first line is an integer, t, indicating the number of test cases.
numTestCases = int(input())

# The t subsequent lines each contain an integer, n.
for tests in range(numTestCases):
    print(findDigits(int(input())))
