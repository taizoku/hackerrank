n = int(input().strip())
a = list(map(int, input().strip().split(' ')))

# bubble sort
numSwaps = temp = 0
print(a)

for i in range(0, n):
    j = i + 1
    if a[i] < a[j]:
        temp = a[i]
        a[i] = a[j]
        a[j] = temp
        numSwaps += 1

firstElement = a[0]
lastElement = a[-1]
print("First:", firstElement, "Last:", lastElement)
