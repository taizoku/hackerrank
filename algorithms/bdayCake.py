def solve(n, s, d, m):
    # s = [2 2 1 3 2]

    s = sorted(s)
    # s = [1 2 2 2 3]
    print(s)
    # remove counts of same number twice
    # s = [1 2 2 3]
    new = True
    onlyTwo = []
    for element in s:
        if element not in onlyTwo:
            new = False
            check = element
            onlyTwo.append(element)

        else:
            if new is False:
                new = True
                onlyTwo.append((element))

            if element == check:
                continue
    print(onlyTwo)

    validCombination = 0

    # m is how many numbers we are adding
    for i in range(len(onlyTwo)):
        for j in range(1, len(onlyTwo)):
            sum = 0
            sum = onlyTwo[i] + onlyTwo[j]
            print(sum)
            # d is the unique sum we want to reach using unique combinations
            if sum == d:
                validCombination += 1

    return validCombination


n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
d, m = input().strip().split(' ')
d, m = [int(d), int(m)]
result = solve(n, s, d, m)
print(result)
