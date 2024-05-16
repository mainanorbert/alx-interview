#!/usr/bin/python3
"""
    Module for Prime Game numbers
"""


def sieve_of_eratosthenes(n):
    """_Functioon that return all prim numbers from 1 to n_

    Args:
        n (_int_): _range of 1 to n_

    Returns:
        _array_: _array of prime numbers_
    """
    primes = [True for _ in range(n + 1)]
    p = 2
    while p * p <= n:
        # If prime[p] is not changed, then it is a prime
        if primes[p] is True:
            # Update all multiples of p
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1
    # Return all prime numbers
    return [p for p in range(2, n + 1) if primes[p]]


def isWinner(x, nums):
    """_determins winner of prime number game_

    Args:
        x (_int_): _no of times to play_
        nums (_array_): _array of numbers used in the game
    """
    if len(nums) == 0 or x == 0 or x is None or nums is None:
        return None
    b_c = 0
    m_c = 0
    rounds = 0
    for no in range(0, x):
        i = nums[no]
        int_array = [vals for vals in range(1, i + 1)]
        flag = True

        prime_array = sieve_of_eratosthenes(i)
        if len(prime_array) == 0:
            b_c += 1
        # Generating ints in give range
        int_array = [vals for vals in range(1, i + 1)]

        for prime in prime_array:
            multiples = []
            first_mul = prime * ((1 + prime - 1) // prime)
            current_mul = first_mul
            while current_mul <= i:
                multiples.append(current_mul)
                current_mul += prime
            # Calculating remaining ints after subtracting multiples
            int_array = [x for x in int_array if x not in multiples]
            if len(int_array) == 1 and int_array[0] == 1:
                if flag is True:
                    m_c += 1
                if flag is False:
                    b_c += 1
            flag = not flag
    if b_c > m_c:
        return "Ben"
    elif m_c > b_c:
        return "Maria"
    else:
        return None


# isWinner(3, [4, 5, 1])
# isWinner(5, [2, 5, 1, 4, 3])
