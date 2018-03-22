import os

def diagonalDifference(a):
    primary = a[0][0] + a[1][1] + a[2][2]
    secondary = a[0][2] + a[1][1] + a[2][0]
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
