import random
import math
n = 879654189120208790204390695024022752539423104564567

i = 1
x = [random.randrange(1, n-1)]
c = random.randrange(1, n-1)
while True:

    x.append((x[i-1]*x[i-1]+c)%n)
    for j in range(1, i-1):
        x_j = x[j-1]*x[j-1]+c
        d = math.gcd(x[i] - x_j, n)
        if d != 1 and d != n:
            break
    else:
        i += 1
        continue
    break
print(d)
if d == 1:
    print(str(n) + " might be prime")
else:
    print(str(d) + " is a factor of " + str(n))
