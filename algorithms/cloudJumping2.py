# https://www.hackerrank.com/challenges/jumping-on-the-clouds-revisited/problem

# Aerith is playing a cloud hopping game.
# In this game, there are sequentially numbered clouds that can be thunderheads or cumulus clouds.
# Her character must jump from cloud to cloud until it reaches the start again.

# To play, Aerith is given an array of clouds, c and an energy level e = 100.
# She starts from c[0]
# -> uses 1 unit of energy to make a jump of size k to cloud c[(i+k) % n]

# If Aerith lands on a thundercloud, c[i]
# -> her energy (e) decreases by 2 additional units.
# The game ends when Aerith lands back on cloud 0.

# Given the values of:
# - n
# - k
# - the configuration of the clouds as an array
# Can you determine the final value of e after the game ends?

# EXAMPLE:
# c = [0, 0, 1, 0]
# k = 2
# the indices of her path are 0 -> 2 -> 0

# Her energy level decreases by 1 for each jump to 98
# She landed on ONE thunderhead = additional cost of 2 energy units
# Therefore, her final energy level is 96

# FUNCTION
def jumpingOnClouds(numClouds, jumpDistance):
    energyLevel = 100

    return energyLevel


# INPUT
# 1. Two space-separated integers:
# - n, the number of clouds
# - k, the jump distance.
numClouds, jumpDistance = map(int, input().strip().split(' '))

# 2. n space-separated integers c[i]
# *Each cloud is described as follows:
# - c[i] = 0: cumulus cloud
# - c[i] = 1: thunderhead
clouds = list(map(int, input().strip().split(' ')))

# OUTPUT (e)
print(jumpingOnClouds(numClouds, jumpDistance))
