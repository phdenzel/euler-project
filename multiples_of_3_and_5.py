#!/usr/bin/env python
from time_and_test import tnt


divisors = [3, 5]


def obvious_solution(upto):
    """
    The most obvious and probably most inefficient solution
    """
    solution = []
    for number in range(0, upto+1):
        if any((number//d)*d == number for d in divisors):
            solution.append(number)
    return sum(solution)


def better_solution(upto):
    """
    A slightly better solution than <obvious_solution>
    """
    solution = []
    for number in range(0, upto+1):
        if any(number % d == 0 for d in divisors):
            solution.append(number)
    return sum(solution)


def euler_divisible(n, upto):
    """
    Use Euler's trick to see if the sum of a series of numbers is divisible by n

    Note:
        - Euler's trick: 1+2+3+...+N = N*(N+1)/2
        - therefore: 3*(1+2+3+...+N) is divisible by 3
    """
    return n*(upto//n)*((upto//n)+1)//2


def euler_solution(upto):
    """
    Use Euler's trick to find an efficient solution

    Note:
        - for only two divisors this would be
          euler_divisible(3, 999) + euler_divisible(5, 999) - euler_divisible(15, 999)
    """
    from functools import reduce
    from itertools import combinations
    from fractions import gcd
    total = sum([euler_divisible(d, upto) for d in divisors])
    # remove multiples
    sign = -1
    for i in range(2, len(divisors)+1):
        for c in combinations(divisors, i):
            product = reduce(lambda x, y: x*y, c)//reduce(gcd, c)
            total += sign*euler_divisible(product, upto)
        sign *= -1
    return total


if __name__ == "__main__":
    N = 1000
    reps = 3
    v = o = True
    arg = 1000-1
    tnt(obvious_solution, args=(arg), repeats=reps, loops=N,
        output=o, verbose=v)
    tnt(better_solution, args=(arg), repeats=reps, loops=N,
        output=o, verbose=v)
    tnt(euler_solution, args=(arg), repeats=reps, loops=N,
        output=o, verbose=v)
