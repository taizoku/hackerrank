import itertools

def solve(numofSquares, array, desiredValue, addLength):
    usedSegment = []
    validCombination = 0

    # should be in range 0 to (n-(m-1)); m being length equal to birth month
    for i in range(numofSquares - (addLength - 1)):

        currentSegment = []
        segmentValue = 0
        # range from 0 to m (length we adding)
        for limit in range(addLength):
            segmentValue += array[i + limit]
            currentSegment.append(array[i + limit])

        if (segmentValue == desiredValue) and currentSegment not in usedSegment:
            usedSegment.append(currentSegment)
            validCombination += 1

    print(usedSegment)

    return validCombination


n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
d, m = input().strip().split(' ')
d, m = [int(d), int(m)]
result = solve(n, s, d, m)
print(result)
