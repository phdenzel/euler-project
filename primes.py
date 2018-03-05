#!/usr/bin/env python
"""
Module containing method for finding primes
"""
import numpy as np


def primes_bruteforce(limit):
    """
    Prime number generator (upto a given limit)
    with a sort-of bruteforce method
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


def eratosthenes(limit):
    """
    Calculate all primes up to limit using the sieve of Eratosthenes method
    """
    if isinstance(limit, (int, float)) and limit == int(limit):
        limit = int(limit)
    else:
        raise ValueError
    primes = []
    mask = [1]*(limit+1)
    for i in range(2, limit+1):
        if mask[i]:
            primes.append(i)
            for j in range(i*i, limit+1, i):
                mask[j] = 0
    return primes


def eratosthenes_np(limit):
    """
    Calculate all primes up to limit using the sieve of Eratosthenes method
    utilizing numpy arrays and methods
    """
    if isinstance(limit, (int, float)):
        limit = int(limit)
    else:
        raise ValueError
    mask = np.ones(limit+1, dtype=np.bool)
    mask[:2] = False
    for i in range(2, int(np.sqrt(limit))+1):
        if mask[i]:
            mask[i*i::i] = False
    return np.nonzero(mask)[0]


def eratosthenes_npo(limit):
    """
    Calculate all primes up to limit using the sieve of Eratosthenes method
    utilizing numpy arrays and methods, trying to conserve memory
    """
    if isinstance(limit, (int, float)):
        limit = int(limit)
    else:
        raise ValueError
    mask = np.ones(limit//2, dtype=np.bool)
    for i in range(3, int(limit**0.5)+1, 2):
        if mask[i//2]:
            mask[i*i//2::i] = False
    return np.r_[2, 2*np.nonzero(mask)[0][1::]+1]
