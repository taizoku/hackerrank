def solve(n, s, d, m):
    sum = 0
    for i in range(n):
        sum += s[i]
        if len(sum) == d:
            if sum == m:


n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
d, m = input().strip().split(' ')
d, m = [int(d), int(m)]
result = solve(n, s, d, m)
print(result)
