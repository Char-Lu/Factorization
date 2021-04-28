from p_rho import factor
from plain_rsa import encode


def crack(N, e, c):
    p,q = factor(N)
    R = (p-1)*(q-1)

    d = pow(e, -1, R)
    return (c ** d) % N


if __name__ == "__main__":
    N = 31*37
    e = 77
    m = 1145
    c = encode(N, e, m)
    print("The coded message is:       " + str(c))
    print("The original message was:   " + str(m))
    print("Given N, e we decoded:      " + str(crack(N, e, c)))