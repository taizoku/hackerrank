# input:
#   - given array of integers
#   - integer k
#
# task:
#   find and print number of (i,j) pairs where
#   i < j and a[i] + a[j] is divisble by k

def divisibleSumPairs(n, k, ar):
    for i in ar:
        if i < j and ar[i] + ar[j] % k == 0:
            add to counter


n, k = input().strip().split(' ')
n, k = [int(n), int(k)]
ar = list(map(int, input().strip().split(' ')))
result = divisibleSumPairs(n, k, ar)
print(result)