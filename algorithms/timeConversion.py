def timeConversion(s):
    twentyFour = s[:-2]
    if s[-2:] == "PM":
        if s[:2] != "12":
            twentyFour = str(int(s[:2]) + 12) + s[2:-2]

    else:
        if s[:2] == "12":
            twentyFour = "00" + s[2:-2]
    return twentyFour


if __name__ == '__main__':
    s = input()
    print(timeConversion(s))
