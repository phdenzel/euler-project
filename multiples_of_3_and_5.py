#!/usr/bin/env python
import timeit

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
    repeats = 3
    arg = 1000-1
    time = timeit.repeat(
        'multiples_of_3_and_5.obvious_solution({})'.format(arg),
        setup="import multiples_of_3_and_5", repeat=repeats, number=N)
    print("obvious_solution({0:}):\t{1:}\n".format(
        arg, obvious_solution(arg))
          + "{0:} loops, best of {1:}:, {2:.4f} usec per loop".format(
              N, repeats, sum(time)/repeats/N*10**6))
    time = timeit.repeat(
        'multiples_of_3_and_5.better_solution({})'.format(arg),
        setup="import multiples_of_3_and_5", repeat=repeats, number=N)
    print("better_solution({0:}):\t{1:}\n".format(
        arg, better_solution(arg))
          + "{0:} loops, best of {1:}:, {2:.4f} usec per loop".format(
              N, repeats, sum(time)/repeats/N*10**6))
    time = timeit.repeat(
        'multiples_of_3_and_5.euler_solution({})'.format(arg),
        setup="import multiples_of_3_and_5", repeat=repeats, number=N)
    print("euler_solution({0:}):\t{1:}\n".format(
        arg, euler_solution(arg))
          + "{0:} loops, best of {1:}:, {2:.4f} usec per loop".format(
              N, repeats, sum(time)/repeats/N*10**6))
