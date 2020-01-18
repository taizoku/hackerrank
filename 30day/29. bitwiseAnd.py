# number of test cases
t = int(input())

for _ in range(t):
    # get space separated input
    # 1. n - defines set length S where S = {1, 2, 3, ... n}
    # 2. k - maximum size of number
    n, k = map(int, input().split())

    answer = None
    for i in range(1, n):
        for j in range(i+1, n+1):
            # print(i, 'AND', j, '=', i&j)
            if i&j > answer and i&j < k:
                answer = i&j
    print(answer)
    
