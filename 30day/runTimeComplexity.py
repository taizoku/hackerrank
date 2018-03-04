# https://www.hackerrank.com/challenges/30-running-time-and-complexity/problem

'''
Background:
A prime is a natural number > 1 that has no positive divisors other than 1 and itself.

Task:
Given a number, n, determine and print whether it's prime or not prime.

Input:
The first line contains an integer, T, the number of test cases.
Each of the T subsequent lines contains an integer, n, to be tested for primality.

Output:
For each test case, print whether n is Prime or Not prime on a new line.
'''

# Take in number of test cases and inputs
testCases = int(input())
for i in range(testCases):
    n = list(int, input().strip().split(' '))

prime = False
for number in n:
    if number % (number/2) != 0:
        prime = True

print("Prime") if prime else print("Not prime")
