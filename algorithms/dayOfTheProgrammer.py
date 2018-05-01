import sys

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


year = int(input().strip())
result = solve(year)
print(result)
