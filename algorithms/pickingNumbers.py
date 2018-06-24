# Given array of numbers
# - find max num of integers you can select from array such that the absolute
# > difference between the any two of the chosen are less than or equal to 1

# Example
# - array = [1, 1, 2, 2, 4, 4, 5, 5, 5]
# - can create TWO sub-arrays
# 1. [1, 1, 2, 2] length = 4
# 2. [4, 4, 5, 5, 5] length = 5
def pickingNumbers(array):
    usedNumbers = list()

    print("array:", array)

    filledArrays = list()

    for i in range(len(array)):
        if array[i] not in usedNumbers:
            currentArray = list()
            currentArray.append(array[i])

            j = i+1
            for element in currentArray:
                while j < len(array):

                    print(element, "-", array[j])
                    if abs(element - array[j]) <= 1:
                        currentArray.append(array[j])

                    j += 1
        else:
            continue

        if len(currentArray) > 1:
            filledArrays.append(currentArray)

    print("full", filledArrays)

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