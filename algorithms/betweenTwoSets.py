def getTotalX(a, b):
    a = sorted(a)
    b = sorted(b)
    stuff = []

    for number in range(a[1], b[0]):
        print(number)
        for first in a:
            if number % first == 0:
                for second in b:
                    if number % second == 0:
                        if number == second[-1]:
                            stuff.append(number)

    # the things in stuff should be factors of all elements in b

    print(stuff)
    return len(stuff)

if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    total = getTotalX(a, b)

    print(total)
