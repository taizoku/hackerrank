def migratoryBirds(n, ar):
    collection = dict()

    for bird in ar:
        if bird not in collection:
            collection[str(bird)] = collection.get(bird, 0)


    print(collection)
    return collection


n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = migratoryBirds(n, ar)
print(result)
