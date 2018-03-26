n = int(input())

ar = list(map(int, input().rstrip().split()))

def birthdayCakeCandles(n, ar):
    canReach = 0
    for candle in sorted(ar):
        if candle == n-1:
            canReach += 1
    return canReach

print(birthdayCakeCandles(n, ar))