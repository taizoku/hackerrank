# A Discrete Mathematics professor has a class of students.
# Frustrated with their lack of discipline,
# he decides to cancel class if fewer than some number of students are present when class starts.
# Arrival times go from on time (arrivalTime <= 0) to arrived late (arrivalTime > 0).

# OUTPUT
# For each test case, print the word YES if the class is canceled or NO if it is not.

# INPUT FORMAT
# 1. t - number of test cases
# * Each test case consists of TWO lines
numTestCases = int(input())

# First line has two SPACE-SEPARATED INTEGERS:
# - n, number of students in class
# - k, cancellation threshold
for i in range(numTestCases):
    numStudents = int(input())
    cancelCondition = int(input())

# Second line contains n space-separated integers (a_1, ... a_n)
# - describes arrival times for each student