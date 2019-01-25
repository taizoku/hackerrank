# HACKER RANK CHALLENGE: https://www.hackerrank.com/challenges/angry-professor/problem
# A Discrete Mathematics professor has a class of students.
# Frustrated with their lack of discipline,
# he decides to cancel class if fewer than some number of students are present when class starts.
# Arrival times go from on time (arrivalTime <= 0) to arrived late (arrivalTime > 0).

# OUTPUT
# For each test case, print the word YES if the class is canceled or NO if it is not.


def angryProfessor(cancelCondition, arrivalTimes):
    outcome = "YES"
    goodStudents = 0
    for present in arrivalTimes:
        if present <= 0:
            goodStudents += 1

    if goodStudents >= cancelCondition:
        outcome = "NO"

    return outcome


# INPUT FORMAT
# 1. t - number of test cases
# * Each test case consists of TWO lines
numTestCases = int(input())

# First line has two SPACE-SEPARATED INTEGERS:
# - n, number of students in class
# - k, cancellation threshold
for i in range(numTestCases):
    numStudents, cancelCondition = map(int, input().strip().split(' '))

# Second line contains n space-separated integers (a_1, ... a_n)
# - describes arrival times for each student
    arrivalTimes = list(map(int, input().strip().split(' ')))

    print(angryProfessor(cancelCondition, arrivalTimes))