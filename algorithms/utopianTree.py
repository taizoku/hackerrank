# The Utopian Tree goes through 2 cycles of growth every year.
# Each spring, it doubles in height.
# Each summer, its height increases by 1 meter.

# Laura plants a Utopian Tree sapling with a height of 1 meter at the onset of spring.
# How tall will her tree be after  growth cycles?

# INPUT:
# The first line contains an integer, t, the number of test cases.
# - subsequent t lines contain integer n denoting num of cycles for that test cases

numTestCases = int(input())

for i in range(numTestCases):
    utopianTree(int(input()))