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
        if year % 4:
            # print("issa leap year according to julian")
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
    if year == 1918:
        # 1918 is NOT a leap year so
            # not a leap year - 28 days
            # feb 14 is 32
            # feb 28 is 46th day -> march 1 is 47th
        marchFirst = 47

    # else year is either < 1918 or > 1918
        # (uses the same logic)
    else:
        if isLeapYear(year):
            # feb 29 is 29+31 = 60th day
            # march 1st is 61st day
            marchFirst = 31 + 29 + 1

        else:
            # feb 28 is 59th day
            marchFirst = 31 + 28 + 1

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

    # month = 3
    # day = 1
    totalDays = 0
    for month in range(9):
        if month == 4 or month == 6:
            totalDays += 30

        if month == 2:
            if year == 1918:
                totalDays += 15

            else:
                if isLeapYear(year):
                    totalDays += 29

                else:
                    totalDays += 28

        else:
            totalDays += 31

    # for i in range(marchFirst, 250):
    #     # if month is april, june or september
    #     if month == 4 or month == 6 or month == 9:
    #         # when day reaches end of month
    #         if day == 30:
    #             # enter new month, reset day
    #             month += 1
    #             day = 1
    #
    #     else:
    #         if day == 31:
    #             month += 1
    #             day = 1
    #
    #     day += 1

    day = 256 - totalDays

    if month < 10:
        month = "0" + str(month)

    date = str(day) + "." + month + "." + str(year)
    return date


year = int(input().strip())
result = solve(year)
print(result)
