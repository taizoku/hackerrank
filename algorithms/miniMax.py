def miniMaxSum(array):
    array = sorted(array)
    min = max = 0
    for i in range(len(array)):
        if i < len(array) - 1:
            min += array[i]

        if i != 0:
            max += array[i]
    print(min, max)


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)