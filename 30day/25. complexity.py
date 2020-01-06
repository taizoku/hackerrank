"""
https://www.hackerrank.com/challenges/30-running-time-and-complexity/problem
"""

import math

def isPrime(n):
    prime = True  # assume the number is prime unless proven otherwise
    for i in range(2, math.floor(math.sqrt(n))+1):
        if n % i == 0:
            prime = False
            break
        
    if prime and n >= 2:  # edge case 1 (not prime), 2 (prime)
        print("Prime")
    else:
        print("Not prime")


num_tests = int(input())

for i in range(num_tests):
    isPrime(int(input()))
