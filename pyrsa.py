import random


def key_gen():
    p = prime_gen(1000)
    q = prime_gen(1000)
    n = p * q
    phi_n = (p - 1) * (q - 1)
    e = e_gen(phi_n)
    d = d_gen(phi_n, e)
    pub_key = (e, n)
    pri_key = (d, n)
    return pub_key, pri_key


def prime_gen(prime_range):
    while True:
        result = random.randint(2, prime_range)
        if result % 2 != 0 and fermat_primality_test(result, 10):
            return result


def fermat_primality_test(m, k):
    for i in range(k):
        a = random.randint(2, m - 2)
        g = ex_euclid(a, m)[0]
        if g == 1:
            r = a ** (m - 1) % m
            if r != 1:
                return False
        else:
            return False
    return True


# def gcd(num1, num2):
#     while num2:
#         num1, num2 = num2, num1 % num2
#     return num1


def e_gen(phi_n):
    while True:
        e = random.randint(2, phi_n)
        if ex_euclid(phi_n, e)[0] == 1:
            return e


def d_gen(phi_n, e):
    return ex_euclid(phi_n, e)[2]


def ex_euclid(a, b):
    if a < b:
        a, b = b, a
    x1, x2, x3 = 1, 0, a
    y1, y2, y3 = 0, 1, b
    while y3 != 0:
        q = x3 // y3
        t1, t2, t3 = x1 - q * y1, x2 - q * y2, x3 - q * y3
        x1, x2, x3 = y1, y2, y3
        y1, y2, y3 = t1, t2, t3
    while x2 < 0:
        x2 = x2 + a
    return x3, x1, x2


def fast_mod(x, a, n):
    a = bin(a)[2:]
    y = 1
    for i in range(len(a)):
        y = y * y % n
        if a[i] == '1':
            y = y * x % n
    return y


def encrypt(m, pub_key):
    return fast_mod(m, pub_key[0], pub_key[1])


def decrypt(c, pri_key):
    return fast_mod(c, pri_key[0], pri_key[1])


if __name__ == '__main__':
    pub, pri = key_gen()
    plain_text = 123
    c = encrypt(plain_text, pub)
    print(c)
    m = decrypt(c, pri)
    print(m)
