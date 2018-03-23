def staircase(n):
    i = 1
    for i in range(n):
        for spaces in range(n-i):
            print(" ", end="")

        for hashtags in range(i):
            print("#", end="")
        print("")

# for i in range(n):
    # if(n-1) > 0:


if __name__ == '__main__':
    n = int(input())

    staircase(n)
