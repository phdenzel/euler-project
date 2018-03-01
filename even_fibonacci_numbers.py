#!/usr/bin/env python
import timeit

def bruteforce_solution(upto):
    """
    A brute-force and probably most inefficient solution
    """
    fibn = 1
    fibnp1 = 1
    total = 0
    while fibn < upto:
        if fibn % 2 == 0:
            total += fibn
        fibnp2 = fibnp1 + fibn
        fibn = fibnp1
        fibnp1 = fibnp2
    return total


def better_solution(upto):
    """
    A slightly smarter solution than <bruteforce_solution>

    Note:
        - Every third Fibonacci number is even (the sum of two odd numbers)
        - Combine three steps into one: Fn = Fn-1 + Fn-2 = ... = 4*Fn-3 + Fn-6
    """
    fibn = 2
    fibnm3 = 2
    fibnm6 = 0
    total = 0
    while fibn < upto:
        total += fibn
        fibn = 4*fibnm3 + fibnm6
        fibnm6 = fibnm3
        fibnm3 = fibn
    return total


def even_fibs(upto):
    fibnm6, fibnm3, fibn = 0, 2, 2
    while fibn < upto:
        yield fibn
        fibn = 4*fibnm3 + fibnm6
        fibnm6 = fibnm3
        fibnm3 = fibn


def generator_solution(upto):
    """
    An attempt to minimize memory usage by using generator,
    and the same strategy as in <better_solution>
    """
    return sum(even_fibs(upto))


if __name__ == "__main__":
    N = 1000
    repeats = 3
    arg = 4000000
    arg = 100000000000000
    time = timeit.repeat(
        'even_fibonacci_numbers.bruteforce_solution({})'.format(arg),
        setup="import even_fibonacci_numbers", repeat=repeats, number=N)
    print("bruteforce_solution({0:}):\t{1:}\n".format(
        arg, bruteforce_solution(arg))
          + "{0:} loops, best of {1:}:, {2:.4f} usec per loop".format(
              N, repeats, sum(time)/repeats/N*10**6))
    time = timeit.repeat(
        'even_fibonacci_numbers.better_solution({})'.format(arg),
        setup="import even_fibonacci_numbers", repeat=repeats, number=N)
    print("better_solution({0:}):\t{1:}\n".format(
        arg, better_solution(arg))
          + "{0:} loops, best of {1:}:, {2:.4f} usec per loop".format(
              N, repeats, sum(time)/repeats/N*10**6))
    time = timeit.repeat(
        'even_fibonacci_numbers.generator_solution({})'.format(arg),
        setup="import even_fibonacci_numbers", repeat=repeats, number=N)
    print("generator_solution({0:}):\t{1:}\n".format(
        arg, generator_solution(arg))
          + "{0:} loops, best of {1:}:, {2:.4f} usec per loop".format(
              N, repeats, sum(time)/repeats/N*10**6))
