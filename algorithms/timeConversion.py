def timeConversion(s):
    if s[-2:] == "PM":
        twelve = str(int(s[:2]) + 12)
        print("change", twelve)
        s[:1] = twelve
    return s

if __name__ == '__main__':
    s = input()

    print(timeConversion(s))
