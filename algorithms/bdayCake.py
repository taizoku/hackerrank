def solve(numofSquares, array, desiredValue, addLength):
    usedSegment = []
    validCombination = 0

    # range from 0 to the number of squares minus the desired length of segments
    # covers the range of all valid segments without extending to a invalid range
    for i in range(numofSquares - (addLength - 1)):
        # stores the current combination that makes up the segment
        currentSegment = []
        # the value of the segment
        segmentValue = 0

        # range from 0 to length of segment -1
        for limit in range(addLength):
            # adds each piece of the segment at each iteration; array[i] + ... array[i+n-1]
            segmentValue += array[i + limit]
            # appends combination to array so we can check it later
            currentSegment.append(array[i + limit])

        # if the segmentValue is what we want and the combination has not been used then
        if (segmentValue == desiredValue) and currentSegment not in usedSegment:
            # add it to the usedSegment pile
            usedSegment.append(currentSegment)
            # and count it as a validCombination
            validCombination += 1

    print(usedSegment)

    return validCombination


n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
d, m = input().strip().split(' ')
d, m = [int(d), int(m)]
result = solve(n, s, d, m)
print(result)
