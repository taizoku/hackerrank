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

    magicNumber = 15 # every permutation should equal this
    permutations = 8 # there are 8 possible magic squares in a 3x3 matrix

    # loop goes through row, col
    for i in range(3):
        for j in range(3):
            print(square[i][j])

    combinatrics = dict()
    id = list()
    threeSum = 0
    for i in range(3):
        for j in range(3):
            threeSum += square[i][j]
            id.append([i, j])
            print(id)

            if j == 2:
                combinatrics[id[0]] = threeSum
                print("yeS", combinatrics[id[0]])
                threeSum = 0 # reset sum of line

    return copy

if __name__ == '__main__':
    s = []
    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    print(formingMagicSquare(s))
