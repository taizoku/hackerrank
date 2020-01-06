n = int(input())

phone_book = {}

for i in range(n):
    information = input().split()
    name = information[0]
    if len(information) is not 1:
        number = information[1]

    else:
        number = None
    phone_book[name] = number

prompt = True
while prompt:
    query = input()
    if query == "quit":
        prompt = False

    if query in phone_book:
        print(query, "=", phone_book.get(query), sep = '')

    else:
        print("Not found")
