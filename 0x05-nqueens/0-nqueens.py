#!/usr/bin/python3
"""
Solves the N queens problem
"""

import sys


def print_usage_and_exit(message):
    """Prints an error message and exits with status 1."""
    print(message)
    sys.exit(1)


def is_safe(board, row, col, n):
    """Check if it's safe to place a queen at board[row][col]."""
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def solve_nqueens(n):
    """Solves the N-Queens problem and prints each solution."""
    def backtrack(row, board):
        if row == n:
            print([[i, board[i]] for i in range(n)])
            return

        for col in range(n):
            if is_safe(board, row, col, n):
                board[row] = col
                backtrack(row + 1, board)
                board[row] = -1

    board = [-1] * n
    backtrack(0, board)


def main():
    if len(sys.argv) != 2:
        print_usage_and_exit("Usage: nqueens N")

    try:
        n = int(sys.argv[1])
    except ValueError:
        print_usage_and_exit("N must be a number")

    if n < 4:
        print_usage_and_exit("N must be at least 4")

    solve_nqueens(n)


if __name__ == "__main__":
    main()
