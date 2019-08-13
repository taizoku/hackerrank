'''
# Task
Your local library needs your help! Given the expected and actual return dates for a library book,
    create a program that calculates the fine (if any). The fee structure is as follows:

1. If the book is returned on or before the expected return date, no fine will be charged (i.e.: 0.
2. If the book is returned after the expected return day but still within the same calendar month
     and year as the expected return date, 15*days late.
3. If the book is returned after the expected return month but still within the same calendar year
     as the expected return date, the 500*months late.
4. If the book is returned after the calendar year in which it was expected, there is a fixed
     fine of 10000.
'''


actualDay, actualMonth, actualYear = map(int, input().split(' '))
dueDay, dueMonth, dueYear = map(int, input().split(' '))

if actualYear <= dueYear:  # if it was returned on the right year or before even
    if actualYear < dueYear:
        fine = 0
    else:
        if actualMonth <= dueMonth:  # returned on the same month
            if actualDay <= dueDay:  # returned before/on the day
                fine = 0
            else:  # late by a few days
                fine = 15*(actualDay - dueDay)
        else:  # same year, but after the month
            fine = 500*(actualMonth - dueMonth)

else:  # we can assume it was a year late (no time travel)
    fine = 10000

print(fine)

# actualDay, actualMonth, actualYear = map(int, input().split(' '))
# dueDay, dueMonth, dueYear = map(int, input().split(' '))
#
# if actualYear < dueYear:  # if it was returned on the right year or before even
#     fine = 0
#
# elif actualYear == dueYear:
#         if actualMonth < dueMonth:  # returned before the month due
#             fine = 0
#
#         # same month
#         elif actualMonth == dueMonth:
#             if actualDay <= dueDay:  # returned before or on the day due
#                 fine = 0
#
#             else:  # late by a few days
#                 fine = 15*(actualDay - dueDay)
#
#         else:  # same year, but after the month
#             fine = 500*(actualMonth - dueMonth)
#
# else:  # we can assume it was a year late (no time travel)
#     fine = 10000
#
# print(fine)