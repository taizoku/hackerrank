n = int(input())

phone_book = {}

for i in range(n):
    name, number = input().split()
    phone_book[name] = number

prompt = True
while prompt:
    query = input()
    if query == "quit":
        prompt = False

    if phone_book.get(query):
        print(number)

    else:
        print(phone_book.get(query))
        print("Not found")
