def aVeryBigSum(n, ar):
    sum = 0
    for i in range(n):
        sum += ar[i]
    return sum


n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = aVeryBigSum(n, ar)
print(result)