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

    b_c = 0
    m_c = 0
    for i in nums:
        int_array = [vals for vals in range(1, i + 1)]
        flag = True

        prime_array = sieve_of_eratosthenes(i)
        if len(prime_array) == 0:
            b_c += 1
            # print('b won')
        int_array = [vals for vals in range(1, i + 1)]
        for prime in prime_array:

            muls = []
            first_mul = prime * ((1 + prime - 1) // prime)
            current_mul = first_mul
            while current_mul <= i:
                muls.append(current_mul)
                current_mul += prime
            # print(flag)
            int_array = [x for x in int_array if x not in muls]
            if len(int_array) == 1 and int_array[0] == 1:
                if flag is True:
                    # print('m won')
                    m_c += 1
                if flag is False:
                    # print('b won')
                    b_c += 1
            flag = not flag
    if b_c > m_c:
        return "Ben"
    else:
        # print("Winner: Maria")
        return "Maria"
    # print(f"b: {b_c}, m: {m_c}")


# isWinner(3, [4, 5, 1])
# isWinner(5, [2, 5, 1, 4, 3])
