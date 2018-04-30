import itertools

def solve(numofSquares, array, desiredValue, addLength):
    usedSegment = []

    validCombination = 0

    # should be in range 0 to (n-(m-1)); m being length equal to birth month
    for i in range(numofSquares):
        if array[i + (addLength - 1)] == None:
            break

        currentSegment = []
        segmentValue = 0
        # range from 0 to m (length we adding)
        for limit in range(addLength):
            segmentValue += array[i + limit]
            currentSegment.append(array[i + limit])

        if (segmentValue == desiredValue) and currentSegment not in usedSegment:
            usedSegment.append(currentSegment)
            # usedSegment.append([array[i], array[i + 1], array[i + 2]])
            validCombination += 1

    print(usedSegment)
    print(list(itertools.permutations(array)))

    return validCombination

    #  # check if segment not already checked
    #     if (s[i], to s[i+m]) not in usedSegment:
    #
    #         if tracking < n:
    #             while i < m:
    #                 if s[i] == d:
    #                     usedSegment.append(,)
    #
    #
    #
    # new = True
    # onlyTwo = []
    # for element in s:
    #     if element not in onlyTwo:
    #         new = False
    #         check = element
    #         onlyTwo.append(element)
    #
    #     else:
    #         if new is False:
    #             new = True
    #             onlyTwo.append((element))
    #
    #         if element == check:
    #             continue
    # print(onlyTwo)
    #
    # validCombination = 0
    #
    # # m is how many numbers we are adding
    # for i in range(len(onlyTwo)):
    #     for j in range(1, len(onlyTwo)):
    #         sum = 0
    #         sum = onlyTwo[i] + onlyTwo[j]
    #         print(onlyTwo[i], "+", onlyTwo[j], "=", sum)
    #         # d is the unique sum we want to reach using unique combinations
    #         if sum == d:
    #             validCombination += 1

n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
d, m = input().strip().split(' ')
d, m = [int(d), int(m)]
result = solve(n, s, d, m)
print(result)
