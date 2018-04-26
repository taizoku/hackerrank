def getTotalX(a, b):
    a = sorted(a)
    b = sorted(b)

    half = []
    satisfied = []

    # find common multiples for first array
    for number in range(a[-1], b[0] + 1):
        for first in a:
            if number % first == 0:
                if first == a[-1]:
                    half.append(number)

            else:
                break
    print(half)

    # check if factor of all in second array
    for check in half:
        for second in b:
            if second % check == 0:
                if second == b[-1]:
                    satisfied.append(check)

            else:
                break

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
