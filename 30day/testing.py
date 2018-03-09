'''
# need at least 5 test cases
# Output:
    YES
    NO
    YES
    NO
    YES
'''


cancellation = False
if n < k:
    cancellation = True
if t <= 5:
    if 3 <= n <= 200:
        if 1 <= k <= n:
            cancellation = True
