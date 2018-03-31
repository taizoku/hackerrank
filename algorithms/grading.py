#!/bin/python3

import os

def gradingStudents(grades):
    for grade in grades:
        if grade(1) < 5 
        if grade > 38 and grade + 5:
            # round to nearest

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    grades = []

    for _ in range(n):
        grades_item = int(input())
        grades.append(grades_item)

    result = gradingStudents(grades)

    f.write('\n'.join(map(str, result)))
    f.write('\n')

    f.close()
