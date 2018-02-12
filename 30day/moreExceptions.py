class Calculator:
    def power(self, n, p):
        # raise ValueError("n and p should be non-negative")
        raise NegativeException
        return pow(n, p)


class NegativeException(Exception):
    def __init__(self):
        if n < 0 or p < 0:
            print("n and p should be non-negative")
        else:
            print(pow(n, p))


myCalculator = Calculator()
T = int(input())
for i in range(T):
    n, p = map(int, input().split())
    try:
        ans = myCalculator.power(n, p)
        print(ans)
    except Exception as e:
        print(e)
