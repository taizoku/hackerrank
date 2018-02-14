n = int(input().strip())
a = list(map(int, input().strip().split(' ')))

# bubble sort
numSwaps = 0
print(a)

for passNum in range(n - 1, 0, -1):
    for i in range(passNum):
        if a[i] < a[i+1]:
            a[i], a[i+1] = a[i+1], a[i]
            numSwaps += 1

print(a)

firstElement = a[0]
lastElement = a[-1]
print("First:", firstElement, "Last:", lastElement)
