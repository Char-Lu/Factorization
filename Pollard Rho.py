import random
import time
import p_rho


if __name__ == "__main__":
    import matplotlib.pyplot as plt

    nums = []
    times = []
    for i in range(4,5):

        t = 0
        for j in range(50):
            n = random.getrandbits(2 ** (i + 1))

            start = time.perf_counter_ns()
            f = p_rho.factor(n)
            stop = time.perf_counter_ns()
            t += abs(stop-start)
            times.append(t)
            nums.append(len(f))
        t=0

    print(nums)
    plt.scatter(nums, times, color='blue', alpha=0.5)
    plt.xlabel("Number of factors")
    plt.ylabel("Time")
    plt.show()

