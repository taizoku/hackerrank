# Given array of numbers
# - find max num of integers you can select from array such that the absolute
# > difference between the any two of the chosen are less than or equal to 1

# Example
# - array = [1, 1, 2, 2, 4, 4, 5, 5, 5] 1 1 2 2 4 4 5 5 5
# - can create TWO sub-arrays
# 1. [1, 1, 2, 2] length = 4
# 2. [4, 4, 5, 5, 5] length = 5
def pickingNumbers(array):
    usedNumbers = list()

    print("array:", array)

    filledArrays = list()

    for i in range(len(array)):
        currentArray = list()
        currentArray.append(array[i])

        for j in range(len(array)):
            # iterate for and check rest!
            if j != i:
                if abs(array[i] - array[j]) <= 1:
                    passed = True
                    for checked in currentArray:
                        if abs(checked - array[j]) > 1:
                            passed = False
                    if passed is True:
                        currentArray.append(array[j])

        if len(currentArray) > 1:
            filledArrays.append(currentArray)

    # recursively - pick number check does it work try another number

    print("full ", filledArrays)

    maxArrayLen = 0
    for current in filledArrays:
        if len(current) > maxArrayLen:
            maxArrayLen = len(current)

    return maxArrayLen


# INPUT
# 1. single integer n (size of array)
n = int(input())

# 2. n space separated integers a[i]
array = list(map(int, input().strip().split(' ')))

# OUTPUT
# max num of integers we can choose from array
print(pickingNumbers(array))