#!/usr/bin/env python
import timeit
from math import floor, log
from primes import primes_upto

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
    primes = primes_upto(max_divisor)
    solution = 1
    for p in primes:
        a = int(floor(log(max_divisor)/log(p)))
        solution = solution * pow(p, a)
    return solution


if __name__ == "__main__":
    N = 10
    repeats = 3
    arg = 2520
    time = timeit.repeat(
        'smallest_multiple.faster_solution({})'.format(arg),
        setup="import smallest_multiple", repeat=repeats, number=N)
    print("faster_solution({0:}):\t{1:}\n".format(
        arg, faster_solution(arg))
          + "{0:} loops, best of {1:}:, {2:.4f} usec per loop".format(
              N, repeats, sum(time)/repeats/N*10**6))
    time = timeit.repeat(
        'smallest_multiple.optimized_solution({})'.format(divisible_upto),
        setup="import smallest_multiple", repeat=repeats, number=N)
    print("optimized_solution({0:}):\t{1:}\n".format(
        divisible_upto, optimized_solution(divisible_upto))
          + "{0:} loops, best of {1:}:, {2:.4f} usec per loop".format(
              N, repeats, sum(time)/repeats/N*10**6))
