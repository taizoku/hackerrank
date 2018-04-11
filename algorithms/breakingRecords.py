def breakingRecords(score):
    highest = lowest = countHigh = countLow = 0
    for game in score:
        if game == score[0]:
            highest = lowest = game

        if game > highest:
           highest = game
           countHigh += 1

        if game < lowest:
            lowest = game
            countLow += 1

    return countHigh, countLow


if __name__ == '__main__':
    n = int(input())

    score = list(map(int, input().rstrip().split()))

    result = breakingRecords(score)

    print(result)
