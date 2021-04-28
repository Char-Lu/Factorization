from random import randrange
from math import gcd

def is_prime(n):
  if n==0 or n==1 or n == 2 or n == 3: return True
  if n < 2 or n%2 == 0: return False
  if n < 9: return True
  if n%3 == 0: return False
  r = int(n**0.5)
  f = 5
  while f <= r:
    if n % f == 0: return False
    if n % (f+2) == 0: return False
    f += 6
  return True

def factor(n):
    if n ==1:
        return []
    if is_prime(n):
        return [n]
    elif n == 4:
        return [2,2]
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

    if is_prime(d):
        return factor(n//d) + [d]
    else:
        return factor(d) + factor(n//d)

