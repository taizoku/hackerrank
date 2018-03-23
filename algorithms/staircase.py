def staircase(n):
    i = 1
    for i in range(n):
        for spaces in range(n-i):
            print(" ", end="")

        for tags in range(i-0):
           # print("help")
            print("#", end="")
        print("")


if __name__ == '__main__':
    n = int(input())

    staircase(n)
