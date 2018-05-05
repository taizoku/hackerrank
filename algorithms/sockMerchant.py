# pile of socks to PAIR by COLOUR

# input:
#   - n: number of socks
#   - ar: array of colours of socks

# task:
# determine how many pairs of socks with matching colours there are

def sock_merchant(num_of_socks, sock_pile):
    sock_pile = sorted(sock_pile)

    i = num_of_pairs = 0
    while i < num_of_socks:
        print("i", i)
        if sock_pile[i] == sock_pile[i+1]:
            num_of_pairs += 1
            i += 2
            print(i)

        else:
            i += 1
        # if sock_pile[i] == sock_pile[i+1]:
        #     sock_pile.pop(i)
        #     sock_pile.pop(i + 1)
        #     num_of_pairs += 1
        #     i += 1

    return num_of_pairs


n = int(input())
arr = map(int, input().strip().split(' '))

print(sock_merchant(n, arr))