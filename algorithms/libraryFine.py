# Your local library needs your help!
# Given the expected and actual return dates for a library book,
# Create a program that calculates the fine (if any).
# The fee structure is as follows:
#   1. If the book is returned on or before the expected return date,
#       no fine will be charged (i.e. fine = 0)
#
#   2. If the book is returned after the expected return day but still within the same calendar
#       month and year as the expected return date, fine = 15 Hackos * (the num of days late).
#
#   3. If the book is returned after the expected return month but still within the same calendar
#       year as the expected return date, fine = 500 Hackos * (the num of months late).
#
#   4. If the book is returned after the calendar year in which it was expected,
#       there is a fixed fine of 10, 000 Hackos.
#
# Charges are based only on the least precise measure of lateness.
#
# EXAMPLE
# Whether a book is due January 1, 2017 or December 31, 2017, if it is returned January 1, 2018,
# that is a year late and the fine would be 10, 000 Hackos


# FUNCTION DESCRIPTION
# Return an integer representing the fine due.

# libraryFine has the following parameter(s):
#   - d1, m1, y1: returned date day, month and year
#   - d2, m2, y2: due date day, month and year
def libraryFine(returnDay, returnMonth, returnYear, dueDay, dueMonth, dueYear):
    fine = 0  # if book returned on or before expected due date
    if returnYear > dueYear:
        fine = 10000  # Hackos

    elif returnYear == dueYear:
        if returnMonth > dueMonth:
            fine = 500 * (returnMonth - dueMonth)

        elif returnMonth == dueMonth:
            if returnDay > dueDay:
                fine = 15 * (returnDay - dueDay)

    return fine


# INPUT FORMAT
# 1. Contains 3 space-separated integers, d1, m1, y1
#       denoting the respective day, month and year on which the book was returned.
returnDay, returnMonth, returnYear = map(int, input().strip().split(' '))

# 2. The second line contains 3 space-separated integers, d2, m2, y2
#       denoting the respective day, month and year on which the book was due to be returned.
dueDay, dueMonth, dueYear = map(int, input().strip().split(' '))

# OUTPUT FORMAT
# Print a single integer denoting the library fine for the book received as input.
print(libraryFine(returnDay, returnMonth, returnYear, dueDay, dueMonth, dueYear))
