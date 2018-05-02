# BACKGROUND
# 1700 to 1917 - Julian Calendar
# 1918 - Julian -> Gregorian
# Feb 14 was the 32nd day of the year (comes after Jan 31)
# 1919 onwards - Gregorian Calendar

# FEBRUARY is the variable month
#   LEAP year = 29 days
#   NOT LEAP year = 28 days

# LEAP YEAR RULES
#   Julian Calendar: leap years divisible by 4
#   Gregorian Calendar: leap years:
#       - divisible by 400
#       - divisible by 4 NOT divisible by 100


def isLeapYear(year):
    leapYear = False
    if year < 1918:
        if year % 4 == 0:
            leapYear = True

    else:
        if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
            # print("issa leap year according to greg")
            leapYear = True
    return leapYear

# TASK
# Given a year find the date of the 256th day
#   print format dd.mm.yyyy


def solve(year):
    jan = 1
    feb = 2
    apr = 4
    jun = 6
    sep = 9

    # NOTE
    # CAN'T BE October, November or December > 256 days
    # 30 days:
    #   - 4 (April)
    #   - 6 (June)
    #   - 9 (September)

    # 31 days:
    #   - 3 (March)
    #   - 5 (May)
    #   - 7 (July)
    #   - 8 (August)

    totalDays = 0
    for month in range(jan, sep):
        if month == apr or month == jun:
            totalDays += 30

        elif month == feb:
            if year == 1918:
                totalDays += 15

            else:
                if isLeapYear(year):
                    totalDays += 29

                else:
                    totalDays += 28

        else:
            totalDays += 31

    day = 256 - totalDays

    date = str(day) + "." + "0" + str(month + 1) + "." + str(year)
    return date


year = int(input().strip())
result = solve(year)
print(result)
