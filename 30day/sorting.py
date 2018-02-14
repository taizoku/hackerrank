n = int(input().strip())
a = list(map(int, input().strip().split(' ')))

# bubble sort
numSwaps = temp = 0
prevNum = 32678
for element in a:
    temp = element
    if element < prevNum:
        element = prevNum
    prevNum = element
