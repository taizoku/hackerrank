def migratoryBirds(n, ar):
    collection = dict()

    for bird in ar:
        if str(bird) not in collection:
            collection[str(bird)] = collection.get(bird, 0)
        collection[str(bird)] = collection[str(bird)] + 1
    return collection


n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = migratoryBirds(n, ar)
print(result)
