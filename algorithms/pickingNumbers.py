# Given array of numbers
# - find max num of integers you can select from array such that the absolute
# > difference between the any two of the chosen are less than or equal to 1

# Example
# - array = [1, 1, 2, 2, 4, 4, 5, 5, 5]
# - can create TWO sub-arrays
# 1. [1, 1, 2, 2] length = 4
# 2. [4, 4, 5, 5, 5] length = 5
def pickingNumbers(array):
    usedNumbers = []

    print("array:", array)
    subArrays = []
    for i in range(len(array)):
        for j in range(1, len(array)):
            if array[i] not in usedNumbers:
                subArrays.append([array[i]])
                usedNumbers.append(array[i])

                if abs(array[i] - array[j]) <= 1:
                    subArrays[i].append(array[j])

    print("subarray:", subArrays)
    return len(array)


# INPUT
# 1. single integer n (size of array)
n = int(input())

# 2. n space separated integers a[i]
array = list(map(int, input().strip().split(' ')))

# OUTPUT
# max num of integers we can choose from array
print(pickingNumbers(array))