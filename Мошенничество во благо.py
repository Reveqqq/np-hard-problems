import random
import math
import time


def power_mod(base, exponent, modulus):
    result = 1
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        base = (base * base) % modulus
        exponent //= 2
    return result


def ferma(x):
    if x == 2:
        return True
    if x < 2 or x % 2 == 0:
        return False

    random.seed(time.time())

    for _ in range(100):
        a = random.randint(2, x - 2)

        if math.gcd(a, x) != 1:
            return False

        if power_mod(a, x - 1, x) != 1:
            return False

    return True


n = int(input())

if ferma(n):
    print('Простое число')
else:
    print('Составное число')
