# given a list of letter heights in the alphabet and a string.
# Using the letter heights given,
# determine the area of the rectangle highlight in mm^2
# - assuming width of letters are all 1mm wide

# input format
# 1. 26 space separated integers
#   - describes heights of each letter [a-z]


def designerPdfViewer(heights, word):
    width = len(word)
    maxHeight = 0
    # height is highest letter height
    for i in range(len(word)):
        print(heights[ord(word[i]) - ord('a')])
        maxHeight = max(maxHeight, heights[ord(word[i]) - ord('a')])
        # print(heights[word[i]])
        # maxHeight = max(maxHeight, heights[word[i]])

    return width*maxHeight


# method 1
heights = list(map(int, input().strip().split(' ')))

# method 2
# noLabel = list(map(int, input().strip().split(' ')))
#
# heights = {}
# i = 0
# for letter in range(ord('a'), ord('z')+1):
#     heights[chr(letter)] = noLabel[i]
#     i += 1

print(heights)

# 2. single word made of lowercase english alphabetic letters
word = input()

print(designerPdfViewer(heights, word))

# output format
# single integer denoting area in mm^2
