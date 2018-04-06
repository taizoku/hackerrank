def kangaroo(x1, v1, x2, v2):
    if x1 > x2 and v2 > v1:
        # print((x1 - x2) % (v2 - v1))
        # should also check if it lies within a multiplicative range
        if (x1 - x2) % (v2 - v1) == 0:
            return "YES"

    elif x1 < x2 and v1 > v2:
        # x1 + v1*t = x2 + v2*t
        # print((x2 - x1) % (v1 - v2))
        if (x2 - x1) % (v1 - v2) == 0:
            return "YES"

    return "NO"


x1, v1, x2, v2 = input().strip().split(' ')
x1, v1, x2, v2 = [int(x1), int(v1), int(x2), int(v2)]
result = kangaroo(x1, v1, x2, v2)
print(result)
