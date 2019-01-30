# Link: https://www.hackerrank.com/challenges/cut-the-sticks/problem

# PROBLEM
# You are given a number of sticks of varying lengths. You will iteratively cut the sticks into smaller sticks,
# discarding the shortest pieces until there are none left. At each iteration you will determine the length of
# the shortest stick remaining, cut that length from each of the longer sticks and then discard all the pieces
# of that shortest length. When all the remaining sticks are the same length, they cannot be shortened so discard them.

Given the lengths of  sticks, print the number of sticks that are left before each iteration until there are none left.

# For example, there are  sticks of lengths . The shortest stick length is , so we cut that length from the longer two and discard the pieces of length . Now our lengths are . Again, the shortest stick is of length , so we cut that amount from the longer stick and discard those pieces. There is only one stick left, , so we discard that stick. Our lengths are .