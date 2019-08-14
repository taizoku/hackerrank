# PROBLEM
# Lilah has a string, s, of lowercase English letters that she repeated infinitely many times.
# Given an integer, n, find and print the number of letter a's in the first n letters of Lilah's infinite string.

# EXAMPLE
# If the string s = 'abcac' and n = 10,
# The substring we consider is 'abcacabcac', the first 10 characters of her infinite string.
# There are 4 occurrences of a in the substring.

# FUNCTION DESCRIPTION
# Complete the repeatedString function in the editor below.
# Return the number of occurrences of a in the prefix of length n in the infinitely repeating string.
#
# repeatedString has the following parameter(s):
# - s: a string to repeat
# - n: the number of characters to consider

# INPUT FORMAT
# The first line contains a single string, s.
# The second line contains an integer, n.

# OUTPUT FORMAT
# Print a single integer denoting the number of letter a's
# in the first n letters of the infinite string created by repeating s infinitely many times.


def repeatedString(string, n):
    if len(string) > 0:  # make sure its not empty
        string *= (n // len(string))+1
        string = string[:n]
    return string.count('a') + string.count('A')


string = input()
n = int(input())
print(repeatedString(string, n))
