class Calculator:
    def power(self, n, p):
        if n < 0 or p < 0:
            print("n and p should be non-negative")
        return pow(n, p)