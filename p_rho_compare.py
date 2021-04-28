
from random import randrange
from math import gcd
import numpy as np
import random
import math
import pandas as pd
import timeit
from sympy import *

def is_prime(n):
    if n== 0 or n == 1 or n == 2 or n == 3: return True
    if n < 2 or n % 2 == 0: return False
    if n < 9: return True
    if n % 3 == 0: return False
    r = int(n ** 0.5)
    f = 5
    while f <= r:
        if n % f == 0: return False
        if n % (f + 2) == 0: return False
        f += 6
    return True


def PR(n):
    if n == 1:
        return []
    if is_prime(n):
        return [n]
    elif n == 4:
        return [2, 2]
    x = randrange(1, n - 1)
    c = randrange(1, n - 1)

    f = lambda x: (x ** 2 + c) % n

    y = f(x)
    d = 1
    while d == 1:
        x = f(x) % n
        y = f(f(y)) % n
        d = gcd(x - y, n)
        if d == n:
            x = randrange(1, n - 1)
            c = randrange(1, n - 1)
    if is_prime(d):
        return PR(n // d) + [d]
    else:
        return PR(d) + PR(n // d)


def reg(n):
    if n == 1:
        return []
    if is_prime(n):
        return [n]
    elif n == 4:
        return [2, 2]
    i = 2
    while (i < n):
        if n % i == 0:
            return [n, n / i]
        i += 1
    return [1, n]


def find_e(R, primes):
    i = 0
    while R % primes[i] == 0:
        i += 1
    return primes[i]


import sympy


def encode(N, e, m):
    c = (m ** e) % N
    return c


def crack1(N, e, c):
    p, q = PR(N)
    R = (p - 1) * (q - 1)
    d = pow(e, -1, int(R))
    return (c ** d) % N


def crack2(N, e, c):
    p, q = reg(N)
    R = (p - 1) * (q - 1)
    d = pow(e, -1, int(R))
    return (c ** d) % N


if __name__ == "__main__":
    nums = []
    primes = list(sympy.primerange(0, 3000))
    for i in range(0,10):
        p = primes[randrange(0,len(primes))]
        q = primes[randrange(0,len(primes))]
        while p == q:
            q = primes[randrange(0,len(primes))]
        N = p*q
        R = (p - 1)*(q - 1)
        e = find_e(R, primes)
        m = randrange(0,100)
        c = encode(N, e, m)
        start = timeit.timeit()
        m1 = crack1(N, e, c)
        end = timeit.timeit()
        start1 = timeit.timeit()
        m2 = crack1(N, e, c)
        end1 = timeit.timeit()
        nums.append([N,R,e,m,c,m1, m2, abs(end - start), abs(end1 - start1)])
    df = pd.DataFrame(data=nums, columns = ['Number','R','e', 'm', 'c', 'm1','m2', 'PR time', 'Reg Time'])
df