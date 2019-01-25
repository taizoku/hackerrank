def staircase(n):
    for i in range(1, n+1):
        for spaces in range(n-i):
            print(" ", end="")

        for tags in range(i):
            print("#", end="")
        print("")


if __name__ == '__main__':
    n = int(input())

    staircase(n)
