def solve(n, s, d, m):
    # s = [2 2 1 3 2]
    usedSegment = []
    #s = sorted(s)
    # s = [1 2 2 2 3]
    print(s)
    # remove counts of same number twice
    # s = [1 2 2 3]

    # variable keeps track of where we are in the maybe??
    tracking = 0
    # should be in range 0 to (n-(m-1)); m being length equal to birth month
    for i in range(n-(m-1)):
        # range from 0 to m (length we adding)
        for limit in range(m):

        # check if segment not already checked
        if (s[i], to s[i+m]) not in usedSegment:
            if tracking < n:
                while i < m:
                    if s[i] == d:
                        usedSegment.append(,)



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
            print(onlyTwo[i], "+", onlyTwo[j], "=", sum)
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
