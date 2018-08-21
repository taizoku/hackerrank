# BACKGROUND
# Aerith is playing a cloud hopping game. In this game, there are sequentially
# numbered clouds that can be thunderheads or cumulus clouds.
# Her character must jump from cloud to cloud until it reaches the start again.

# PROBLEM
# To play, Aerith is given an array of clouds, c and an energy level e = 100.
# She starts from c[0] and uses 1 unit of energy to make a jump of size k to cloud c[(i+k) % n].
# If Aerith lands on a thundercloud, c[i] = 1, her energy (e) decreases by 2 additional units.
# The game ends when Aerith lands back on cloud 0.

# Given the values of n, k, and the configuration of the clouds as an array c,
# - Can you determine the final value of e after the game ends?
