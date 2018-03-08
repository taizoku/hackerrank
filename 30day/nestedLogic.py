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

actualData = list(map(int, input().split(' ')))
expectedData = list(map(int, input().split(' ')))

print("actualData:", actualData, "| expectedData: ", expectedData)
actualDay = actualData[0]
actualMonth = actualData[1]
actualYear = actualData[2]

expectedDay = expectedData[0]
expectedMonth = expectedData[1]
expectedYear = expectedData[2]

if (actualYear <= expectedYear) and (actualMonth <= expectedMonth) and (actualDay <= expectedDay):
    fine = 0

else:
    if expectedYear == actualYear:
        if expectedMonth == actualMonth:
            daysLate = expectedDay - actualDay
            fine = 15*daysLate

        else:
            monthsLate = expectedMonth - actualMonth
            fine = 500*monthsLate

    elif actualYear > expectedYear:
        fine = 10000

print(fine)
