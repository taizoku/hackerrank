'''
https://www.hackerrank.com/contests/w36/challenges/acid-naming

    Conditions for naming an acid:
    - If the given input starts with hydro and ends with ic then it is a non-metal acid.
    - If the input only ends with ic then it is a polyatomic acid.
    - If it does not have either case, then output not an acid.
'''

#!/bin/python3


import sys


def acidNaming(acid_name):
    # print(acid_name)
    classification = 'not an acid'
    if acid_name[:5] == 'hydro' and acid_name[-2:] == 'ic':
        classification = 'non-metal acid'

    elif acid_name[-2:] == 'ic':
        classification = 'polyatomic acid'

    return classification


if __name__ == "__main__":
    n = int(input().strip())
    for a0 in range(n):
        acid_name = input().strip()
        result = acidNaming(acid_name)
        print(result)
