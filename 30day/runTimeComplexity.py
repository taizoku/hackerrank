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


def isPrime(number):
    # AKS PRIMALITY ALGORITHM
    if number == 2 or number == 3:
        return True

    if number % 2 == 0 or number % 3 == 0:
        return False

    i = 5
    w = 2
    while i * i <= number:
        if n % 1 == 0:
            return False

        i += w
        w = 6 - w
    return True


# Take in number of test cases and inputs
n = []
testCases = int(input())
for i in range(testCases):
    n.append(int(input()))
    # n = list(map(int, input().strip().split(' ')))

for number in n:
    print("Prime") if isPrime(number) else print("Not prime")

'''
for number in n:
    divisor = number-1
while divisor > 1:
    print(divisor, "%", number, ":", (number % divisor))
    if number % divisor == 0:
        prime = False
        break

    else:
        prime = True

    divisor -= 1
'''
