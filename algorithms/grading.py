#!/bin/python3

import os

def gradingStudents(grades):
    i = 0
    for grade in grades:
        if grade > 35:
            rounded = grade + 5 - int(str(grade)[1])

            if int(str(grade)[1]) > 5:
                rounded = grade + 10 - int(str(grade)[1])
                # if grade(1) > 2 and grade(1) < 5 or grade(1) > 7 and grade(1) < 10:
            if rounded > 38:
                if rounded - grade < 3:
                    grades[i] = rounded
        i += 1
    return grades


if __name__ == '__main__':

    n = int(input())

    grades = []

    for _ in range(n):
        grades_item = int(input())
        grades.append(grades_item)

    result = gradingStudents(grades)

    print(result)
