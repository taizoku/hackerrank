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
    n = list(map(int, input().strip().split(' ')))

for number in n:
    divisor = number
    while divisor > 1:
        if divisor % number == 0:
            prime = False
            break

        else:
            prime = True
            
        divisor -= 1

print("Prime") if prime else print("Not prime")
