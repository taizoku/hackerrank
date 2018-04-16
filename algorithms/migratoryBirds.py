from collections import Counter

def migratoryBirds(n, ar):
    counter = Counter(ar)
    for i in counter:
        for j in range(1, n):
            
            if counter[i] == counter[j]:
                lowest = i

    print(counter)
    return lowest


n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = migratoryBirds(n, ar)
print(result)
