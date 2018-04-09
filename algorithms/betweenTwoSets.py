def getTotalX(a, b):
    b = sorted(b)
    # all factors of the integer being considered
    for first in a:
        for second in b:

            if second % stuff != 0:
                remove element lol
            print("mod func or something")

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    total = getTotalX(a, b)

    f.write(str(total) + '\n')

    f.close()
