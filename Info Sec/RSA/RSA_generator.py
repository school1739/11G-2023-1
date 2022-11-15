import math
from random_prime_generator import random_prime


def generate_keys(p=random_prime(2**128, 2**129), q=random_prime(2**128, 2**129)):
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 0
    for e in range(2, phi):
        if math.gcd(e, phi) == 1:
            break
    d = pow(e, -1, phi)

    print(f'p   = {p}\n'
          f'q   = {q}\n'
          f'n   = {n}\n'
          f'phi = {phi}\n'
          f'e   = {e}\n'
          f'd   = {d}\n'
          f'pub = {(e, n)}\n'
          f'prv = {(d, n)}')

    return (e, n), (d, n)


public_key, private_key = generate_keys()
with open('public_key.txt', 'w') as file:
    file.write(f'{public_key[0]} {public_key[1]}')
with open('private_key.txt', 'w') as file:
    file.write(f'{private_key[0]} {public_key[1]}')
