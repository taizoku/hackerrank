# input:
#   - given array of integers
#   - integer k
#
# task:
#   find and print number of (i,j) pairs where
#   i < j and a[i] + a[j] is divisble by k


def divisibleSumPairs(n, k, ar):
    validPairs = 0

    for i in range(n):
        j = i+1
        while j < len(ar):
            if (ar[i] + ar[j]) % k == 0:
                validPairs += 1
            j += 1
    return validPairs


n, k = input().strip().split(' ')
n, k = [int(n), int(k)]
ar = list(map(int, input().strip().split(' ')))
result = divisibleSumPairs(n, k, ar)
print(result)