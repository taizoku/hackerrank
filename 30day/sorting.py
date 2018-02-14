n = int(input().strip())
a = list(map(int, input().strip().split(' ')))

# bubble sort
numSwaps = temp = j = 0
print(a)

for a in range(0, n):
    if a[j] > a[j+1]:
        temp = a[j]
        a[j] = a[j+1]
        a[j+1] = temp
        numSwaps += 1
firstElement = a[0]
lastElement = a[-1]
