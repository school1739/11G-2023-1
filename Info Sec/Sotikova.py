import random


def nsd(a, b):
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a

    if a + b == 1:
        return True
    else:
        return False


def bpow(a, b):
    if b == 0:
        return 1
    elif b % 2 == 1:
        return bpow(a, b - 1) * a
    else:
        c = bpow(a, b / 2)
        return c * c


while True:
    p = random.randint(50, 1000)
    q = random.randint(50, 1000)
    if nsd(p, q) == True:
        break

print("p = ", p)
print("q = ", q)

n = p * q

elr = (p - 1) * (q - 1)

while True:
    e = random.randint(2, elr)
    if nsd(e, elr) == True:
        break

d = 2
while True:
    if (e * d) % elr == 1:
        break
    else:
        d += 1
        if d == e:
            d += 1

print("n = ", n)
print("elr = ", elr)
print("e = ", e)
print("d = ", d)
