#!/usr/bin/env python
from math import floor, log
from time_and_test import tnt
from primes import eratosthenes_npo

divisible_upto = 20
divisors = list(range(1, divisible_upto+1))


def obvious_solution(number):
    """
    The most obvious and probably most inefficient solution

    Note:
        - takes way too long to execute...
    """
    while any(number % d != 0 for d in divisors):
        number += 1


def faster_solution(step):
    """
    A faster solution; note that step should be smartly chosen,
    e.g. 2520 for testing divisibility by numbers upto 20
    """
    for number in range(step, 10**14, step):
        if all(number % n == 0 for n in divisors):
            return number
    return None


def optimized_solution(max_divisor):
    """
    Fastest solution I can think of...

    Let's write down the first few cases for k:=max_divisor and N:=solution
    k=2, N=2
    k=3, N=6=2*3
    k=4, N=12=2*2*3
    Thus, we can use prime factorization to solve our problem for higher k.
    The solution can be expressed as an Einstein summation of N = p_i**a_i
    We start by putting a_i=0 for all i, then for divisors j=1,2,3,...,20,...:
    N_j=p_m**b_m where m<j and then a_i=max(a_i, b_i).
    a_i is the largest natural number for which p_i**a_i <= k,
    therefore a_i=floor(log(k)/log(p_i)).
    """
    primes = eratosthenes_npo(max_divisor)
    solution = 1
    for p in primes:
        a = int(floor(log(max_divisor)/log(p)))
        solution = solution * pow(p, a)
    return solution


if __name__ == "__main__":
    N = 10
    reps = 3
    v = o = True
    arg = 2520
    tnt(faster_solution, args=(arg), repeats=reps, loops=N,
        output=o, verbose=v)
    tnt(optimized_solution, args=(divisible_upto), repeats=reps, loops=N,
        output=o, verbose=v)
