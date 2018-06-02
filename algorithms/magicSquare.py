# define magic square to be:
#   - n*n matrix of distinct positive integers

# Replace any number a in the 3x3 matrix with b
#   - at minimal cost abs(a-b)

# Realised it's actually just how little I can change and still have a magic number at MIN COST
# check row, col, diagonal is 15

def formingMagicSquare(square):
    # [0,0][0,1][0,2]
    # [1,0][1,1][1,2]
    # [2,0][2,1][2,2]
    print(square)

    magicNumber = 15

    # loop goes through row, col
    for i in range(3):
        for j in range(3):
            print(square[i][j])

    total = 0
    lowestSum = 1000
    # first row
    if square[0][0] + square[0][1] + square[0][2] != magicNumber:
        # try [0][0]
        total += ()
    # second row
    if square[1][0] + square[1][1] + square[1][2] != magicNumber
    # third row
    if square[2][0] + square[2][1] + square[2][2] != magicNumber

    # first vertical
    if square[0][0] + square[1][0] + square[2][0] != magicNumber
    # second vertical
    if square[0][1] + square[1][1] + square[2][1] != magicNumber
    # third vertical
    if square[0][2] + square[1][2] + square[1][3] != magicNumber

    # first diagonal \
    if square[0][0] + square[1][1] + square[2][2] != magicNumber
    # second diagonal /
    if square[1][2] + square[1][1] + square[2][0] != magicNumber

    return square


s = []

for _ in range(3):
    s.append(list(map(int, input().strip().split())))

print(formingMagicSquare(s))