#!/bin/python3

import os

def gradingStudents(grades):
    for grade in grades:
        rounded = grade + abs(5 - grade[1])
            # if grade(1) > 2 and grade(1) < 5 or grade(1) > 7 and grade(1) < 10:
        if rounded - grade < 3:
            grade
            # round to nearest
    return grades


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
