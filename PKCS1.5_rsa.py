import random

p = 31
q = 37
N = p*q
R = (p-1)*(q-1)
e = 77
d = 533
length_r = 3


#This encode method represents what gets done to the message before sending to receiver
def encode(m):
    r = "1"
    for i in range(length_r-1):
        r += str(random.randint(0, 1))
    print("Random binary of length 3: " + r)
    rm = int(r + str(m),2)
    print("Concatenated random 3 bits + message is: {0:b}".format(rm))

    c = (rm**e) % N
    print("What gets sent in: " + str(c))
    return c


print('Enter message in binary: ', end='')
m = int(input())
c = encode(m)

print("======Decode======")
decode_m = "{0:b}".format((c**d) % N)
print(decode_m)
print("Receiver and sender agreed upon first 3 bits being random (for security). \n"
      "Receiver now knows the message you wanted to send was: " + decode_m[3:])
