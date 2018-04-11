def breakingRecords(score):
    countHigh = countLow = 0
    firstEntry = True

    for game in score:
        if game >= 0:
            if firstEntry:
                firstEntry = False
                highest = lowest = game

            if game > highest:
                highest = game
                countHigh += 1

            elif game < lowest:
                lowest = game
                countLow += 1

    return countHigh, countLow


if __name__ == '__main__':
    n = int(input())

    score = list(map(int, input().rstrip().split()))

    result = breakingRecords(score)

    print(result[0], result[1])
