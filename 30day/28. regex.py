import re

n = int(input())

text = ""
for _ in range(n):
    text += input()
    text += '\n'

print(text)

# filter for gmails only
pattern = re.compile('([a-z]{1,20})\s([a-z@\.]{1,40}@gmail\.com)')

# find emails out of given input
matches = pattern.findall(text)

# sort alphabetically
names = sorted([i[0] for i in matches])

for name in names:
    print(name)

    
