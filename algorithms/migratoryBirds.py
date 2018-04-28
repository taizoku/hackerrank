#from collections import Counter

def migratoryBirds(n, ar):
    mostFreq = -1
    final = [0, 1, 2, 3, 4, 5]
    counter = 0
    for bird in ar:
        counter += 1
    # counter = Counter(ar)
    #for i in counter(1, n):
     #   for j in range(2, n):
      #      if counter[i] > mostFreq:
       #         mostFreq = i
        #        if counter[i] == counter[j]:
         #           mostFreq = i

    return mostFreq


n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = migratoryBirds(n, ar)
print(result)
