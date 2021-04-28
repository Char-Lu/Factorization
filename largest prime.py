import random
import time

import sympy

import p_rho_once


if __name__ == "__main__":
    import matplotlib.pyplot as plt
    ns = []
    nums = []
    times = []
    primes = list(sympy.primerange(0, 3000))

    for i in range(20):
        # n = random.randrange(2 ** 8, 2 ** (9))
        p = primes[random.randrange(0,len(primes))]
        q = primes[random.randrange(0,len(primes))]
        while p == q:
            q = primes[random.randrange(0,len(primes))]
        n = p*q

        t = 0
        for j in range(30):
            start = time.perf_counter_ns()
            f = p_rho_once.factor(n)
            stop = time.perf_counter_ns()
            t += abs(stop - start)
        ns.append(n)
        times.append(t/30)
        t = 0
        nums.append(f)


    print(ns)
    print(nums)
    print(times)
    plt.scatter(nums, times, color='blue', alpha=0.5)
    plt.xlabel("Value Factored")
    plt.ylabel("Time")
    plt.show()

