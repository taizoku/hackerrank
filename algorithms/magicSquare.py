# define magic square to be:
#   - n*n matrix of distinct positive integers

# Replace any number a in the 3x3 matrix with b
#   - at minimal cost abs(a-b)

# Realised it's actually just how little I can change and still have a magic number at MIN COST
    # MAGIC NUMBER is 15

def formingMagicSquare(square):
    print(square)
    # loop goes through row, col
    for i in range(3):
        for j in range(3):
            print(square[i][j])
            # rules
            # check row, col, diagonal is 15
    square[0][0] + square[0][1] + square[0][2] == 15


    return square


s = []

for _ in range(3):
    s.append(list(map(int, input().strip().split())))

print(formingMagicSquare(s))