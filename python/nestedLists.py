"""
https://www.hackerrank.com/challenges/nested-list/problem
"""

n = int(input())
students = []
for i in range(n):
    name = input()
    grade = float(input())
    students.append([name, grade])

students.sort(key=lambda x: x[1])  # sorts by grade

grades = sorted(set([i[1] for i in students]))  # gives me grades as a set sorted lowest to highest
key = grades[1]

answer = sorted([i[0] for i in students if i[1] == key])

for i in answer:
    print(i)



