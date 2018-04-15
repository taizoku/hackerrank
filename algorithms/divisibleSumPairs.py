# input:
#   - given array of integers
#   - integer k
#
# task:
#   find and print number of (i,j) pairs where
#   i < j and a[i] + a[j] is divisble by k

def divisibleSumPairs(n, k, ar):
    # Complete this function


n, k = input().strip().split(' ')
n, k = [int(n), int(k)]
ar = list(map(int, input().strip().split(' ')))
result = divisibleSumPairs(n, k, ar)
print(result)