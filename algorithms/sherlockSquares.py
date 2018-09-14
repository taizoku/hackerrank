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
    numSq = 0
    # The way I'm going to tackle this is to get the higher square and subtract the lower square
    # from that then add 1 to give me the number of squares in that range
    print(lower == 1)
    while upper >= lower and (not(math.sqrt(lower).is_integer()) or not((math.sqrt(upper)).is_integer())):
        print((math.sqrt(lower)).is_integer())
        if lower == 0 or lower == 1 or not((math.sqrt(lower)).is_integer()):  # if lower is NOT a perfect square
            lower += 1  # move forwards
        print("low", lower)
        if not((math.sqrt(upper)).is_integer()):  # if upper is NOT a perfect square
            upper -= 1  # move backwards
            
    print("u:", upper, "l:", lower)
    if lower != 0 and upper > lower:
        numSq = int(math.sqrt(upper) - math.sqrt(lower)) + 1
    return numSq


# INPUT FORMAT
# The first contains q; number of test cases
numTestCases = int(input())

# Next q lines contain TWO SPACE-SEPARATED INTEGERS a and b; starting and ending integers in the ranges.
for i in range(numTestCases):
    start, end = map(int, input().strip().split(' '))
    print(squares(start, end))