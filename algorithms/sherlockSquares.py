import math

# BACKGROUND
# Watson likes to challenge Sherlock's math ability.
# He will provide a starting and ending value describing a range of integers.
# Sherlock must determine the number of square integers within that range, inclusive of the endpoints.

# NOTE
# A square integer is an integer which is the square of an integer, e.g. 1, 4, 9, 16, 25

# EXAMPLE
# The range is a = 24 and b = 49, inclusive.
# There are three square integers in the range: 25, 36 and 49.


# FUNCTION DESCRIPTION
# Return an integer representing the number of square integers in the inclusive range from a to b.
# squares() has parameters:
#   - a: an integer, the lower range boundary
#   - b: an integer, the upper range boundary
def squares(lower, upper):
    # The way I'm going to tackle this is to get the higher square and subtract the lower square
    # from that then add 1 to give me the number of squares in that range
    highestSquare = math.floor(math.sqrt(upper))
    lowestSquare = math.ceil(math.sqrt(lower))

    return highestSquare - lowestSquare + 1


# INPUT FORMAT
# The first contains q; number of test cases
numTestCases = int(input())

# Next q lines contain TWO SPACE-SEPARATED INTEGERS a and b; starting and ending integers in the ranges.
for i in range(numTestCases):
    start, end = map(int, input().strip().split(' '))
    print(squares(start, end))
