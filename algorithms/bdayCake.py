def solve(n, s, d, m):
    # s = [2 2 1 3 2]
    validCombination = sum = 0

    s = sorted(s)
    # s = [1 2 2 2 3]

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

    # check if sum elements (2) == 4
    # add to counter

    for i in range(m)
        for element in onlyTwo:

            sum += s[i]
        # m is how many numbers we are adding

        # d is the unique sum we want to reach using unique combinations
        if len(sum) == d:
                validCombination += 1
    return validCombination


n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
d, m = input().strip().split(' ')
d, m = [int(d), int(m)]
result = solve(n, s, d, m)
print(result)
