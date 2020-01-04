"""
https://www.hackerrank.com/challenges/30-running-time-and-complexity/problem
"""

import math

def isPrime(n):
    prime = True
    for i in range(2, math.floor(math.sqrt(n))):
        if n % i == 0:
            prime = False
            print("Not prime")
            break
    if prime:
        print("Prime")


num_tests = int(input())

for i in range(num_tests):
    isPrime(int(input()))
