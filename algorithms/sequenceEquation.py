# You are given a sequence of  integers:
# p(1), p(2), ..., p(n)
# Each element in the sequence is distinct and satisfies 1 <= p(x) <= n

# PROBLEM
# For each x where 1 <= x <= n, find any integer y such that p(p(y)) === x and print value y on a new line

# EXAMPLE
# Given sequence p = [5 2 1 3 4] For each value of x between 1 and 5, we analyse:
# * x=1 : p[3],p[4] = 3 so p[p[4]] = 1
# * x=2 : p[2],p[2] = 2 so p[p[2]] = 2
# * x=3 : p[4],p[5] = 4 so p[p[5]] = 3
# * x=4 : p[5],p[1] = 5 so p[p[1]] = 4
# * x=5 : p[1],p[3] = 3 so p[p[3]] = 5
# Essentially, the format is y = [p[location of number wanted in sequence], p[location of location address]]
#
# Therefore, we find the values [4 2 5 1 3] for y

