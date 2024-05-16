#!/usr/bin/python3
"""
Solution to the nqueens problem
"""
import sys


def backtrack(r, n, cols, pos, neg, board):
    """
    backtrack function to find solution
    """
    if r == a:
        res = []
        for l in range(len(board)):
            for k in range(len(board[l])):
                if board[l][k] == 1:
                    res.append([l, k])
        print(res)
        return

    for c in range(a):
        if c in cols or (r + c) in pos or (r - c) in neg:
            continue

        cols.add(c)
        pos.add(r + c)
        neg.add(r - c)
        board[r][c] = 1

        backtrack(r+1, a, cols, pos, neg, board)

        cols.remove(c)
        pos.remove(r + c)
        neg.remove(r - c)
        board[r][c] = 0


def nqueens(a):
    """
    Solution to nqueens problem
    Args:
        a (int): number of queens. Must be >= 4
    Return:
        List of lists representing coordinates of each
        queen for all possible solutions
    """
    cols = set()
    pos_diag = set()
    neg_diag = set()
    board = [[0] * a for b in range(a)]

    backtrack(0, a, cols, pos_diag, neg_diag, board)


if __name__ == "__main__":
    a = sys.argv
    if len(a) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        aa = int(a[1])
        if aa < 4:
            print("N must be at least 4")
            sys.exit(1)
        nqueens(aa)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
