def isLeapYear(year):
    leapYear = False
    if year < 1918:
        if year % 4:
            leapYear = True

    else:
        if year % 400 == 0 and year % 4 == 0 and year % 100 != 0:
            leapYear = True

    return leapYear

def solve(year):
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

    # TASK
    # Given a year find the date of the 256th day
    #   print format dd.mm.yyyy

    if year < 1918:
        if isLeapYear(year):
            grandTotal = 31+29

        else:
            grandTotal = 31+28

    elif year == 1918:
        # if it's a leap year - 29 days
        if isLeapYear(year):
            # feb 14 is 32
            # feb 29 is 47th day
            month = 3
            day = 1
            marchFirst = 48

        else:
            # not a leap year - 28 days
            # feb 29 is 
            marchFirst

        for i in range(marchFirst, 256 + 1):
            if month == 3 or month == 5 or month == 7 or month == 8:
                if day == 31:
                    month += 1
                    day = 1

            else:
                if day == 30:
                    month += 1
                    day = 1


        date = str(day) + "." + str(month) + "." + str(year)
    return date


year = int(input().strip())
result = solve(year)
print(result)
