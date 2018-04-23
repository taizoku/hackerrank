def countApplesAndOranges(houseStart, houseEnd, appleTree, orangeTree, apples, oranges):
    appleCount = orangeCount = 0
    house = list(range(houseStart, houseEnd + 1))
    print(house)

    for apple in apples:
        if apple > 0:
            if (appleTree + apple) in house:
                appleCount += 1

    for orange in oranges:
        if orange < 0:
            if (orangeTree + orange) in house:
                orangeCount += 1

    print(appleCount)
    print(orangeCount)


if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apple = list(map(int, input().rstrip().split()))

    orange = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apple, orange)
