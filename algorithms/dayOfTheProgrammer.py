def solve(year):
    print("Year..")
    # 1700 to 1917 use the Julian Calendar
    # 1918 Transition from Julian->Gregorian
    #   Next day after January 31st was Feb 14
    #   in 1918 Feb 14 was the 32nd day of the year
    # 1919 onwards they use the Gregorian Calendar
    # For both calendars February was the variable months
    #   leap year 29 days
    #   other year 28 days
    #   Julian Calendar: leap years divisible by 4
    #   Gregorian Calendar: leap years:
    #       divisible by 400
    #       divisible by 4 not divisible by 100

    # Given a year find the date of the 256th day
    # print format dd.mm.yyyy

    # Note:
    # Can't be October, November or December
    # 30 days: April June September
    # 31 days: Jan, March, May, July, August,

    if year < 1918:

    elif year == 1918:
        # if it's a leap year
        if year % 400 == 0 and year % 4 == 0 and year % 100 != 0:
            # 29 days in feb
            # feb 14 is 32
            # feb 29 is 47th day
        month = 2
        (day, month, year)

        else:





year = int(input().strip())
result = solve(year)
print(result)
