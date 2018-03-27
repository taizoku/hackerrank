def timeConversion(s):
    twentyFour = s[:-2]
    if s[-2:] == "PM":
        twentyFour = str(int(s[:2]) + 12) + s[2:-2]
    return twentyFour

if __name__ == '__main__':
    s = input()
    print(timeConversion(s))
