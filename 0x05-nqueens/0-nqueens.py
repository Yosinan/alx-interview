#!/usr/bin/python3
"""N queens problem"""

import argparse

'''is_safe: checks if a queen can be placed in a position'''


def is_safe(board, row, col, N):
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i] == col:
            return False
        # Check diagonals
        if abs(i - row) == abs(board[i] - col):
            return False
    return True


def solve_nqueens(N):
    """Solves the N queens problem"""
    if N < 4:
        print("N must be at least 4")
        exit(1)
    solutions = []
    board = [-1] * N

    def solve(row):

        if row == N:
            solutions.append([(i, board[i]) for i in range(N)])
            return

        for col in range(N):
            if is_safe(board, row, col, N):
                board[row] = col
                solve(row + 1)
                board[row] = -1
    solve(0)
    return solutions


def main():
    parser = argparse.ArgumentParser(description="N queens problem solver")
    parser.add_argument(
        "N", type=int, help="Number of queens (must be at least 4)")
    args = parser.parse_args()

    N = args.N
    solutions = solve_nqueens(N)

    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()
