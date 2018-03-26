n = int(input())

ar = list(map(int, input().rstrip().split()))

def birthdayCakeCandles(n, ar):
    canReach = 0
    largest = sorted(ar)[-1]
    for candle in sorted(ar):
        if candle == largest:
            canReach += 1
    return canReach

print(birthdayCakeCandles(n, ar))