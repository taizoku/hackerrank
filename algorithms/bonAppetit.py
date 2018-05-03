# agree to split bill evenly
# brian wants to order something anna is allergic to
#   - anna wont pay for that
# brian gets the check and calculates Anna's portion

# assume bill = [2, 4, 6]
# anna refuses to eat item k = bill[2] which costs 6
# brian calculates that anna will pay (2+4)/2 = 3
# including cost of bill[2] it is (2 + 4 + 6)/2 = 6
#   in case 2 he should refund 3 to Anna

def checkAppetit():
    result = charged - actual

    result = "Bon Appetit"

    return result

# input format:
# space separated integers
#   - n: num of items ordered
#   - k: index of item anna didn't eat
n, k = input()

# bill[i] array
bill = []
for i in range(n):
    bill[i] = input()

# integer b - amount of money brian charged Anna for share of bill
b = int(input())

print(checkAppetit())

# output:
# if fair print "Bon Appetit"
# else print amount needed to refund


