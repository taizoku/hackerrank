'''
https://www.hackerrank.com/challenges/30-exceptions-string-to-integer/problem

Task
Read a string, S, and print its integer value; if S cannot be converted to an integer, print Bad String.
'''

# !/bin/python3


S = input().strip()

try:
    print(int(S))

except ValueError:
    print("Bad string")

