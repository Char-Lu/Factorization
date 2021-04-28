import random
import math


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

def like_random_factor(n):

    if is_prime(n):
        return [n]
    elif n == 4:
        return [2,2]
    i = 1
    x = [random.randrange(1, n-1)]
    c = random.randrange(1, n-1)
    while True:

        x.append((x[i-1]*x[i-1]+c)%n)
        for j in range(1,i-1):
            x_j = x[j-1]*x[j-1]+c
            d = math.gcd(x[i] - x_j, n)
            print(d)
            if d != 1 and d != n:
                break
        else:
            i += 1
            continue
        break
    if is_prime(d):
        return like_random_factor(n//d) + [d]
    else:
        return like_random_factor(d) + like_random_factor(n//d)

def random_factor(n):
    if is_prime(n):
        return [n]
    elif n == 4:
        return [2,2]
    i = 1
    x = [random.randrange(1, n-1)]
    while True:
        x.append(random.randrange(1, n-1))
        for j in range(0,i-1):
            d = math.gcd(x[i] - x[j], n)
            if d != 1 and d != n:
                break
        else:
            i += 1
            continue
        break
    if is_prime(d):
        return random_factor(n // d) + [d]
    else:
        return random_factor(d) + random_factor(n // d)

print(random_factor(100))