# A jail has a number of prisoners and a number of treats to pass out to them.
# Their jailer decides the fairest way to divide the treats is to seat the prisoners
# around a circular table in sequentially numbered chairs.

# A chair number will be drawn from a hat.
# Beginning with the prisoner in that chair,
# one candy will be handed to each prisoner sequentially around the table until all have been distributed.

# The jailer is playing a little joke, though.
# The last piece of candy looks like all the others, but it tastes awful.
# Determine the chair number occupied by the prisoner who will receive that candy.


# EXAMPLE
# For example, there are 4 prisoners and 6 pieces of candy.
# The prisoners arrange themselves in seats numbered 1 to 4.
# Let's suppose two is drawn from the hat.
# Prisoners receive candy at positions 2, 3, 4, 1, 2, 3.
# The prisoner to be warned sits in chair number 3.
def saveThePrisoner(numPrisoners, numSweets, currentChair):
    # last one is the BAD SWEET!

    # currentChair is the STARTING position

    print(list(range(1, numPrisoners+1)))

    while numSweets > 1:
        if currentChair+1 < numPrisoners:
            currentChair += 1
        else:
            currentChair -= 1

        numSweets -= 1

    return currentChair


# INPUT
numTestCases = int(input())
# 1. The FIRST LINE contains an INTEGER, t, denoting the number of test cases.

for test in range(numTestCases):
    # 2. The next t lines each contain 3 SPACE-SEPARATED INTEGERS:
    #   - n: the number of prisoners
    #   - m: the number of sweets
    #   - s: the chair number to start passing out treats at
    numPrisoners, numSweets, startChair = map(int, input().strip().split(' '))

    # OUTPUT
    # For each test case, print the chair number of the prisoner who receives the awful treat on a new line.
    print(saveThePrisoner(numPrisoners, numSweets, startChair))