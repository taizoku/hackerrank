#from collections import Counter

def migratoryBirds(n, ar):
    frequencies = [0, 0, 0, 0, 0, 0]
    for bird in ar:
        frequencies[bird] += 1

    highestValue = -1
    mostFreq = -1
    for i in range(1, 5+1):
        if frequencies[i] > highestValue:
            highestValue = frequencies[i]
            mostFreq = i

    print(frequencies)
    return mostFreq


n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = migratoryBirds(n, ar)
print(result)
