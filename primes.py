#!/usr/bin/env python
"""
Module containing method for finding primes
"""


def primes_upto(limit):
    """
    Prime number generator (upto a given limit)
    """
    primes = [2]
    for i in range(3, limit+1, 2):
        j = 0
        is_prime = True
        while primes[j]*primes[j] <= i:
            if i % primes[j] == 0:
                is_prime = False
                break
            j += 1
        if is_prime:
            primes.append(i)
    return primes
