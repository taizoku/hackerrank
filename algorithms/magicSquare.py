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

    # loop goes through row, col
    for i in range(3):
        for j in range(3):
            print(square[i][j])


    # first row
    square[0][0] + square[0][1] + square[0][2] == 15
    # second row
    square[1][0] + square[1][1] + square[1][2] == 15
    # third row
    square[2][0] + square[2][1] + square[2][2] == 15

    # first vertical
    square[0][0] + square[1][0] + square[1][2] == 15
    # second vertical

    # first diagonal down
    square[0][0] + square[1][1] + square[2][2] == 15

    return square


s = []

for _ in range(3):
    s.append(list(map(int, input().strip().split())))

print(formingMagicSquare(s))