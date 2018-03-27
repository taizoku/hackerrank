def timeConversion(s):
    if s[-2:] == "PM":
        print("24-Hour Time")
    print(s[-2:])
    return

if __name__ == '__main__':
    s = input()

    print(timeConversion(s))
