test_cases = int(input())

strings = []
for i in range(test_cases):
    strings.append(list(input()))

resolved = []
for string in strings:
    even = ""
    odd = ""
    i = 0

    for letter in string:
        if i % 2 == 0:
            even += letter
        else:
            odd += letter
        i += 1
    resolved.append(even + " " + odd)

for results in resolved:
    print(results)