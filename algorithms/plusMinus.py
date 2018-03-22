def plusMinus(arr):
    size = len(arr)
    positive = negative = 0

    for number in arr:
        if number > 0:
            positive += 1
        if number < 0:
            negative += 1

    positive /= size
    negative /= size
    zero = 1 - positive - negative

    print(positive)
    print(negative)
    print(zero)

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
