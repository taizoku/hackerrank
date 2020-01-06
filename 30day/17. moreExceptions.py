class Calculator:
    def power(self, n, p):
        # raise ValueError("n and p should be non-negative")
        if n < 0 or p < 0:
            raise NegativeException
        return pow(n, p)


class NegativeException(Exception):
    def __init__(self):
        # print("n and p should be non-negative")
        super().__init__("n and p should be non-negative")


myCalculator = Calculator()
T = int(input())
for i in range(T):
    n, p = map(int, input().split())
    try:
        ans = myCalculator.power(n, p)
        print(ans)
    except Exception as e:
        print(e)
