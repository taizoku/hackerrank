# agree to split bill evenly
# brian wants to order something anna is allergic to
#   - anna wont pay for that
# brian gets the check and calculates Anna's portion

# assume bill = [2, 4, 6]
# anna refuses to eat item k = bill[2] which costs 6
# brian calculates that anna will pay (2+4)/2 = 3
# including cost of bill[2] it is (2 + 4 + 6)/2 = 6
#   in case 2 he should refund 3 to Anna

# output:
# if fair print "Bon Appetit"
# else print amount needed to refund


def checkAppetit(numOfItems, notEatenIndex, bill, amountCharged):
    print(bill)
    shouldBeCharged = 0
    bill.remove(bill[notEatenIndex])

    for i in range(numOfItems - 1):
        shouldBeCharged += bill[i]

    shouldBeCharged //= 2

    if amountCharged == shouldBeCharged:
        result = "Bon Appetit"

    else:
        result = amountCharged - shouldBeCharged

    return result


# input format:
# space separated integers
#   - n: num of items ordered
#   - k: index of item anna didn't eat
n, k = map(int, input().strip().split(' '))

# bill[i] array
bill = list(map(int, input().strip().split(' ')))

# integer b - amount of money brian charged Anna for share of bill
b = int(input())

print(checkAppetit(n, k, bill, b))
