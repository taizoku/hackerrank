n = int(input().strip())
a = list(map(int, input().strip().split(' ')))

# bubble sort
numSwaps = 0

for passNum in range(n - 1, 0, -1):
    for i in range(passNum):
        if a[i] < a[i+1]:
            a[i], a[i+1] = a[i+1], a[i]
            numSwaps += 1

print("Array is sorted in", numSwaps, "swaps.")
print("First Element:", a[0])
print("Last Element:", a[-1])
# firstElement = a[0]
# lastElement = a[-1]
