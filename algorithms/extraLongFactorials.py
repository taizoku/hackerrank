# BACKGROUND
# The factorial of the integer n, written n!, is defined as:
#   n! = n * (n-1) * (n-2) * ... * 3 * 2 * 1

# PROBLEM
# Calculate and print the factorial of a given integer.

# EXAMPLE
# if n = 30:
#   - calculate 30 * 29 * 28 * ... * 2 * 1
#   - we get: 265252859812191058636308480000000

# FUNCTION DESCRIPTION
# Complete the extraLongFactorials function in the editor below. It should print the result and return.
def extraLongFactorials(integer):
    # python handles big integers already so no need to specify a long or anything
    if integer == 1:
            return 1
    return integer * extraLongFactorials(integer-1)


# extraLongFactorials has the following parameter(s):
#   - n: an integer
integer = int(input())

extraLongFactorials(integer)
# NOTE
# Factorials of  can't be stored even in a  long long variable.
# Big integers must be used for such calculations.
# Languages like Java, Python, Ruby etc. can handle big integers,
#   but we need to write additional code in C/C++ to handle huge values.
# RECOMMENDED: solve this challenge using BigIntegers.
