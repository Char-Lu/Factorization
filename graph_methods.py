import random
import time
import trivial
import p_rho


if __name__ == "__main__":
    import matplotlib.pyplot as plt

    nums = []
    times = []
    triv_nums = []
    triv_times = []
    for i in range(9,10):

        t = 0
        for j in range(1):
            n = random.getrandbits(2 ** (i + 1))

            start = time.perf_counter_ns()
            f = p_rho.factor(n)
            stop = time.perf_counter_ns()
            t += abs(stop-start)
        times.append(t/100)
        nums.append(i+1)
        t=0
        for j in range(1):
            n = random.getrandbits(2 ** (i + 1))

            start = time.perf_counter_ns()
            f = trivial.trivial_factorize(n)
            stop = time.perf_counter_ns()
            t += abs(stop-start)
        triv_times.append(t/100)
        triv_nums.append(i+1)
    print(nums)
    plt.scatter(nums, times, color='blue', alpha=0.5)
    plt.scatter(triv_nums, triv_times, color='red', alpha=0.5)
    plt.xlabel("Number of bits")
    plt.ylabel("Time")
    plt.show()

