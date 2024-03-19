#!/usr/bin/python3
"""Minimum Operations"""


def minOperations(n):
    """function that implements Minimum Operation algorithms"""
    if n == 1:
        return 0

    operations = []
    for i in range(2, n+1):
        while n % i == 0:
            operations.append(i)
            n //= i

    if len(operations) == 0:
        return 0

    return sum(operations)
