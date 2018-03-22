import os

def diagonalDifference(a):
    print("diagonal calculations go here")
    primary = a[0] + a[4] + a[8]
    secondary = a[2] + a[4] + a[6]
    print(abs(primary - secondary))

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    a = []

    for _ in range(n):
        a.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(a)

    f.write(str(result) + '\n')

    f.close()
