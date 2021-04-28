from random import randrange
from math import gcd

def factor(n):
    if n ==1:
        return 1
    x = randrange(1, n-1)
    c = randrange(1, n-1)

    f = lambda x: (x**2 + c) % n

    y = f(x)
    d = 1
    while d == 1:
        x = f(x) % n
        y = f(f(y)) % n
        d = gcd(x-y, n)
        if d == n:
            x = randrange(1, n - 1)
            c = randrange(1, n - 1)

    return d

