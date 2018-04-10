def getTotalX(a, b):
    a = sorted(a)
    b = sorted(b)
    satisfied = []

    for number in range(a[1], b[0]):
        for first in a:

            if number % first == 0:
                print("second stage:", number)

                for second in b:
                    if second % number == 0:
                        if first == a[-1] and second == b[-1]:
                            satisfied.append(number)

    # the things in stuff should be factors of all elements in b

    print(satisfied)
    return len(satisfied)

if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    total = getTotalX(a, b)

    print(total)
