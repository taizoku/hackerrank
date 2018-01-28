#!/bin/python3

import sys


n = int(input().strip())
binary = []
counter = 0
prev = 0

while n > 0:
    remainder = n % 2
    n //= 2
    binary.append(remainder)

check = False
onlyOne = False
print(binary)

for a, b in zip(binary, binary[1:]):
    if onlyOne is False and a == 1:
        counter += 1
        onlyOne = True

    elif a == b == 1:
        counter += 1
print(counter)

'''
for numbers in binary:
    prev = numbers
    if check is True:
        if prev == 1 and instance == False:
            counter += 1
            instance = True

        elif prev == numbers == 1:
            counter += 1
        check = False

    else:
        check = True
print(counter)
'''
'''
result = ''
result += str(binary.pop())
for numbers in binary:
    result += str(numbers)
print(result)
'''
