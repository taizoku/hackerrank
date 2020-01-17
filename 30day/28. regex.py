import re

n = int(input())

for _ in range(n):
    

# filter for gmails only
pattern = re.compile('([a-z]{1,20})\s([a-z]{1,40}@gmail\.com)')

# find emails out of given input
matches = pattern.findall('riya riya@gmail.com julia julia@julia.me julia sjulia@gmail.com')

# sort alphabetically
names = sorted([i[0] for i in matches])

for name in names:
    print(name)

    
