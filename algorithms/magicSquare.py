# define magic square to be:
#   - n*n matrix of distinct positive integers

# Replace any number a in the 3x3 matrix with b
#   - at minimal cost abs(a-b)

# On closer observation, and looking at the example problems, looks like they only replace one number in the row
#    - might be a good place to start!

def formingMagicSquare(square):
    return square


s = []

for _ in range(3):
    s.append(list(map(int, input().strip().split())))

print(formingMagicSquare(s))