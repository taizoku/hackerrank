# given a list of letter heights in the alphabet and a string.
# Using the letter heights given,
# determine the area of the rectangle highlight in mm^2
# - assuming width of letters are all 1mm wide

# input format
# 1. 26 space separated integers
#   - describes heights of each letter [a-z]

def designerPdfViewer(alphaHeights, word):
    area = 0
    width = len(word)

    # height is highest letter height
    for i in range(len(word)+1):
        word[0] = alphaHeights[[0]]

    height = word[0]

    return width*height

noLabel = list(map(int, input().strip().split(' ')))

alphaHeights = {}
i = 0
for letter in range(ord('a'), ord('z')+1):
    alphaHeights[chr(letter)] = noLabel[i]
    i += 1

# or no storing required ord(letter) - ord('a')

print(alphaHeights)

# 2. single word made of lowercase english alphabetic letters
word = input()

print(designerPdfViewer(alphaHeights, word))

# output format
# single integer denoting area in mm^2
