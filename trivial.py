def trivial_factorize(n):
    factors = []
    i = 2
    while i <= (n**(1/2)):
        if n % i == 0:
            factors.append(i)
            n = n//i
        else:
            i += 1
    return factors + [n]

