def kangaroo(x1, v1, x2, v2):
    if x1 > x2:
        if isinstance(x1 / v2, int):
            return "YES"

    else:
        if isinstance(x2 / v1, int):
            return "YES"

    return "NO"


x1, v1, x2, v2 = input().strip().split(' ')
x1, v1, x2, v2 = [int(x1), int(v1), int(x2), int(v2)]
result = kangaroo(x1, v1, x2, v2)
print(result)
