"""
https://www.hackerrank.com/challenges/nested-list/problem
"""

students = []  # store student lists: [name, grade]
for _ in range(int(input()):
    name = input()
    grade = float(input())
    students.append([name, grade])

students.sort(key=lambda x: x[1])  # sort students by grade

grades = sorted(set([i[1] for i in students]))  # gives me grades as a set sorted lowest to highest
key = grades[1]  # identify second lowest grade

answer = sorted([i[0] for i in students if i[1] == key])  # find students with second lowest grade and sort alphabetically

for i in answer:
    print(i)  # now print students
