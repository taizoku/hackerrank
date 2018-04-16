def migratoryBirds(n, ar):
    collection = dict()
    for bird in ar:
        collection[str(bird)] = collection.get(bird, 1) + 1
    print(collection)
    return collection


n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = migratoryBirds(n, ar)
print(result)
