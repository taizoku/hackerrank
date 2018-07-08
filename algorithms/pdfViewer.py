# given a list of letter heights in the alphabet and a string.
# Using the letter heights given,
# determine the area of the rectangle highlight in mm^2
# - assuming width of letters are all 1mm wide

# input format
# 1. 26 space separated integers
#   - describes heights of each letter [a-z]
noLabel = list(map(int, input().strip().split(' ')))

alphaHeights = {}
i = 0
for letter in range(ord('a'), ord('z')+1):
    alphaHeights[chr(letter)] = noLabel[i]
    i += 1

print(alphaHeights)

# 2. single word made of lowercase english alphabetic letters
word = input()

# output format
# single integer denoting area in mm^2
