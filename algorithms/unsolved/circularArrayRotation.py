# circularArrayRotation has the following parameter(s):
# - a: an array of integers to rotate
# - k: an integer, the rotation count
# - queries: an array of integers, the indices to report

# INPUT FORMAT
# The first line contains 3 space-separated integers:
# 1. n (the number of elements in the integer array)
# 2. k (the rotation count)
# 3. queries (the number of queries)

# The second line contains  space-separated integers, where each integer i describes array element a[i].
# Each of the q subsequent lines contains a single integer denoting m, the index of the element to return from a.

import os


# Complete the circularArrayRotation function below.
def circularArrayRotation(a, k, queries):
    b = list(a)
    for i in range(len(a)):
        b[i - (len(a) - k)] = a[i]  # b is shifted a now

    c = list()
    for q in queries:
        c.append(b[q])
    return c


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nkq = input().split()

    n = int(nkq[0])

    k = int(nkq[1])

    q = int(nkq[2])

    a = list(map(int, input().rstrip().split()))

    queries = []

    for _ in range(q):
        queries_item = int(input())
        queries.append(queries_item)

    result = circularArrayRotation(a, k, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

