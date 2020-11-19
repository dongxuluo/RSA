import random


# 密钥的产生
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


# 素数的产生
def prime_gen(prime_range):
    while True:
        result = random.randint(2, prime_range)
        if result % 2 != 0 and fermat_primality_test(result, 10):
            return result


# 费马素性检验
def fermat_primality_test(m, k):
    for i in range(k):
        a = random.randint(2, m - 2)
        # g = gcd(a, m)
        g = ex_euclid(a, m)[0]
        if g != 1:
            return False
        else:
            # r = a ** (m - 1) % m
            r = fast_mod(a, m - 1, m)
            if r != 1:
                return False
    return True


# # 欧几里得算法
# def gcd(a, b):
#     while b:
#         a, b = b, a % b
#     return a


# e的产生, 1 < e < phi_n, gcd(phi_n, e) = 1
def e_gen(phi_n):
    while True:
        e = random.randint(2, phi_n)
        # if gcd(e, phi_n) == 1:
        if ex_euclid(phi_n, e)[0] == 1:
            return e


# d的产生, d * e === 1 mod phi_n
def d_gen(phi_n, e):
    return ex_euclid(phi_n, e)[2]


# 扩展欧几里得算法
def ex_euclid(a, b):
    """
    :param a: 整数
    :param b: 整数, a > b >= 0
    :return: gcd(a, b), x0, y0, 使得ax0 + by0 = gcd(a, b)
    """
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


# 快速模平方算法
def fast_mod(x, a, n):
    """
    :param x: 整数
    :param a: 整数, a > 0
    :param n: 整数, n > 1
    :return: x ** a mod n
    """
    a = bin(a)[2:]
    y = 1
    for i in range(len(a)):
        y = y * y % n
        if a[i] == '1':
            y = y * x % n
    return y


# 加密
def encrypt(plain_text, pub_key):
    return fast_mod(plain_text, pub_key[0], pub_key[1])


# 解密
def decrypt(cipher_text, pri_key):
    return fast_mod(cipher_text, pri_key[0], pri_key[1])


if __name__ == '__main__':
    pub, pri = key_gen()
    plain = 123
    c = encrypt(plain, pub)
    print(c)
    m = decrypt(c, pri)
    print(m)
