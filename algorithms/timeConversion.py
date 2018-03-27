def timeConversion(s):
    if s[-2:] == "PM":
         # s[:1] = str(int(s[:1]) + 12)
    print(str(int(str("12"))+2))
    return

if __name__ == '__main__':
    s = input()

    print(timeConversion(s))
