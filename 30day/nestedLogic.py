'''
# Task
Your local library needs your help! Given the expected and actual return dates for a library book,
    create a program that calculates the fine (if any). The fee structure is as follows:

1. If the book is returned on or before the expected return date, no fine will be charged (i.e.: .
2. If the book is returned after the expected return day but still within the same calendar month
     and year as the expected return date, .
3. If the book is returned after the expected return month but still within the same calendar year
     as the expected return date, the .
4. If the book is returned after the calendar year in which it was expected, there is a fixed
     fine of .
'''

input = []
for i in range(0, 5):
    input = input().split(' ')

print(input)
info = {}
info['returnDay'] = input[0]
input['returnMonth'] = input[1]
input['returnYear'] = input [2]
input['expectedDay'] = input[3]
input['expectedMonth'] = input[4]
input['expectedYear'] = input[5]

if (returnYear <= expectedYear) and (returnMonth <= expectedMonth) and (returnDay <= expectedDay)
daysLate = expected - returned
hackos = 15
fine = hackos * daysLate

print(fine)
