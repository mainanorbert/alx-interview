#!/usr/bin/env python3
""" N queens"""
import sys


def is_safe(board, row, col, N):
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check upper diagonal on right side
    for i, j in zip(range(row, -1, -1), range(col, N)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens(board, row, N, solutions):
    if row == N:
        # Convert board to list of queen positions and add to solutions
        solution = []
        for i in range(N):
            for j in range(N):
                if board[i][j] == 1:
                    solution.append([i, j])
        solutions.append(solution)
        return

    for col in range(N):
        if is_safe(board, row, col, N):
            board[row][col] = 1
            solve_nqueens(board, row + 1, N, solutions)
            board[row][col] = 0


def nqueens(N):
    board = [[0 for _ in range(N)] for _ in range(N)]
    solutions = []
    solve_nqueens(board, 0, N, solutions)
    return solutions


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./0-nqueens.py N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = nqueens(N)
    for solution in solutions:
        print(solution)
