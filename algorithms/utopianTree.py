# The Utopian Tree goes through 2 cycles of growth every year.
# Each spring, it doubles in height.
# Each summer, its height increases by 1 meter.

# Laura plants a Utopian Tree sapling with a height of 1 meter at the onset of spring.
# How tall will her tree be after n growth cycles?


def utopianTree(numCycles):
    height = 1
    for i in range(numCycles):
        # spring is every odd n
        if i % 2 != 0:
            # height doubles
            height *= height

        # summer for every even
        else:
            # height increases by 1
            height += 1

    return height


# INPUT:
# The first line contains an integer, t, the number of test cases.
# - subsequent t lines contain integer n denoting num of cycles for that test cases

numTestCases = int(input())

for i in range(numTestCases):
    print(utopianTree(int(input())))
    