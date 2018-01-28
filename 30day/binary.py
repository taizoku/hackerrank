#!/bin/python3

import sys


n = int(input().strip())
binary = []
counter = max_counter = 0

#Conversion from Decimal to Binary
while n > 0:
    remainder = n % 2
    n //= 2
    binary.append(remainder)

#print(binary)

# for a, b in zip(binary, binary[1:]):
for number in binary:
    # MAXIMUM NUMBER OF CONSECUTIVE ONES
    if number == 1:
        counter += 1
        if counter > max_counter:
            max_counter = counter

    else:
        counter = 0

print(max_counter)

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
