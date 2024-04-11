#!/usr/bin/python3
"""N queens puzzel"""

import sys


def nqueen_puzzle():
    """N queens"""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    n_queen = sys.argv[1]
    try:
        n_queen = int(n_queen)
    except ValueError:
        print('N must be a number')
        sys.exit(1)
    if n_queen < 4:
        print("N must be at least 4")
        sys.exit(1)


nqueen_puzzle()
