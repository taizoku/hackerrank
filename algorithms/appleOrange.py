def countApplesAndOranges(s, t, a, b, apples, oranges):
    appleCount = orangeCount = 0
    house = range(s, t)
    print(house)

    for apple in apples:
        if a + apples in house:
            appleCount += 1

    for orange in oranges:
        if b + orange in house:
            orangeCount += 1

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
