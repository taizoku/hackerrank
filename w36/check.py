'''
https://www.hackerrank.com/contests/w36/challenges/ways-to-give-a-check
    - In this problem, the task is to implement a very simple pawn promotion
        component that can be used in a chess engine.

    - For clarity, White promotes the Pawn by moving it from the -th to the
        -th rank(row) along the same file (column). There are  possible
        different promotions: the pawn can be promoted either to a Queen,
        or to a Rook, or to a Bishop, or to a Knight.

    Input Format
        - In the first line, there is a single integer denoting the number
            of scenarios to handle. After that, descriptions of subsequent scenarios are given.

        - Each scenario consists of 8 lines, with 8 characters each. The first line denotes the
            -th rank (row) on the board, while the last line denotes the -st rank. Empty cells
            on the board are denoted by "#", while pieces are denoted by characters for White's
            pieces and  for Black's pieces, where  is the King, is a Queen, is a Knight, is a Bishop,
            is a Rook, and  is a Pawn).

    Output Format
        - Print exactly  lines. In the -th of them, print a single integer denoting the answer to the
            -th scenario, i.e. the number of ways to promote the pawn resulting in a check in this scenario.
'''

#!/bin/python3

import sys

def waysToGiveACheck(board):
    # out put like so

if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        board = []
        for board_i in range(8):
           board_t = [str(board_temp) for board_temp in input().strip().split(' ')]
           board.append(board_t)
        result = waysToGiveACheck(board)
        print(result)