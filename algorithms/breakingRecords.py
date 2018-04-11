def breakingRecords(score):
    #
    # Write your code here.
    #

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    score = list(map(int, input().rstrip().split()))

    result = breakingRecords(score)

    f.write(' '.join(map(str, result)))
    f.write('\n')

    f.close()
