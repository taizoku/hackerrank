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
returnDay = input[0]
returnMonth = input[1]
returnYear = input [2]

expectedDay = input[3]
expectedMonth = input[4]
expectedYear = input[5]

if (returnYear <= expectedYear) and (returnMonth <= expectedMonth) and (returnDay <= expectedDay):
    daysLate = 0

else:
    if (returnMonth == expectedMonth):
        hackos = 15
        daysLate = expected - returned
        fine = hackos * daysLate

    elif(returnYear == expectedYear):
        hackos = 500

    elif(returnYear > expectedYear):
        fine = 10000

print(fine)
