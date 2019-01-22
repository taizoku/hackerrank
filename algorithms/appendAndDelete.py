# PROBLEM
# Given a string of lowercase English alphabetic letters.
# You can perform two types of operations on the string:
#   1. Append a lowercase English alphabetic letter to the end of the string.
#   2. Delete the last character in the string.
#   **Performing this operation on an empty string results in an empty string.
#
# Given:
# - integer k,
# - strings s
# - string t
# -> Determine whether or not you can convert s to t by performing exactly k of the above operations on s.
# If it's possible, print Yes. Otherwise, print No.

# EXAMPLE
# strings s = [a, b, c] and t = [d, e, f].
# Our number of moves, k = 6.
#
# To convert s to t, we first delete all of the characters in 3 moves.
# Next we add each of the characters of t in order. On the 6th move, you will have the matching string. If there
# had been more moves available, they could have been eliminated by performing multiple deletions on an empty string.
# If there were fewer than 6 moves, we would not have succeeded in creating the new string.


# FUNCTION DESCRIPTION
# Function should return a string, either Yes or No.
def appendAndDelete(initString, finalString, numOperations):
    initString = list(initString)
    finalString = list(finalString)
    same = "No"

    while numOperations > 0:
        if len(initString) > len(finalString):  # reduce first string to the same length as the second
            initString.pop()  # delete the last character until they are the same length
            numOperations -= 1
            continue  # should count as an operation, so it skips to the next count of the loop

        else:
            break

    if numOperations > 0:
        # once they're the same length, now we want to check up to what letters are the same
        for i in range(0, len(initString)):
            if initString[i] != finalString[i]:
                break  # loop until you reach the mismatching letter

        # now we need to continue to pop off characters until they are the same
        # should only be done once procedurally
        while numOperations > 0 and len(initString) != i:
            # first get rid of the ones which aren't the same

                initString.pop()
                numOperations -= 1
                print(initString)

        print(numOperations)
        while numOperations > 0:
            # then we need to add characters so they're identical
            if len(initString) != len(finalString):
                initString.append(finalString[i])
                i += 1

            print(initString)
            print(finalString)
            if initString == finalString:
                same = "Yes"
                break

    return same



# INPUT FORMAT (lines)
# 1. string s, the initial string.
initialString = str(input())

# 2. string t, the desired final string.
finalString = str(input())

# 3. integer k, the number of operations.
numOperations = int(input())

# appendAndDelete has the following parameter(s):
#   - s: the initial string
#   - t: the desired string
#   - k: an integer that represents the number of operations
print(appendAndDelete(initialString, finalString, numOperations))