#from collections import Counter

def migratoryBirds(n, ar):
    frequencies = [0, 0, 0, 0, 0, 0]
    for bird in ar:
        frequencies[bird] += 1

    highestValue = 0
    mostFreq = -1
    for i in range(1, 5):
        if frequencies[i] > highestValue:
            highestValue = frequencies[i]
            mostFreq = i
        # elif frequencies[i] == highestValue:

    # counter = Counter(ar)
    #for i in counter(1, n):
     #   for j in range(2, n):
      #      if counter[i] > mostFreq:
       #         mostFreq = i
        #        if counter[i] == counter[j]:
         #           mostFreq = i

    print(frequencies)
    return mostFreq


n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = migratoryBirds(n, ar)
print(result)
