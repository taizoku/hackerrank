# import os
def diagonalDifference(a):
    i = primary = secondary = 0
    j = -1
    for array in a:
        primary += array[i]
        secondary += array[j]
        i += 1
        j -= 1
    return abs(primary - secondary)


if __name__ == '__main__':
    # f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    a = []

    for _ in range(n):
        a.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(a)

    print(str(result))

    #f.write(str(result) + '\n')
    #f.close()
