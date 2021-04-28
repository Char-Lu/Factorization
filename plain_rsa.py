#This encode method represents what gets done to the message before sending to receiver
import sympy

primes = list(sympy.primerange(0, 100))
def encode(N, e, m):
    c = (m ** e) % N
    return c

def find_e(R):
    i = 0
    while R % primes[i] == 0:
        i += 1
    return primes[i]

if __name__ == "__main__":


    p = 31
    q = 37
    N = p * q
    R = (p - 1) * (q - 1)
    e = 77
    d = 533

    print(find_e(R))


    print('Enter message: ', end='')
    m = int(input())
    c = encode(N, e, m)
    print("What gets sent in: " + str(c))

    print("======Decode======")
    print((c**d)%N)
