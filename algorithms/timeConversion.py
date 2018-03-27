def timeConversion(s):
    if s[-2:] == "PM":
        twelve = s[:1]
        s[:1] = str(int(twelve) + 12)
    return

if __name__ == '__main__':
    s = input()

    print(timeConversion(s))
