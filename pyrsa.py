import random


# 密钥的产生
def key_gen():
    p = prime_gen()
    q = prime_gen()
    n = p * q
    phi_n = (p - 1) * (q - 1)
    e = e_gen(phi_n)
    d = ext_euclid(phi_n, e)[2]
    pub_key = (e, n)
    pri_key = (d, n)
    return pub_key, pri_key


# 大素数的产生
def prime_gen():
    while True:
        prime = random.randint(3, 1000)  # p, q的选取在1000以内
        if prime % 2 != 0 and fermat_primality_test(prime, 10):
            return prime


# 费马素性检验
def fermat_primality_test(m, k):
    for i in range(k):
        a = random.randint(2, m - 2)
        # g = euclid(a, m)
        g = ext_euclid(a, m)[0]
        if g != 1:
            return False
        else:
            # r = a ** (m - 1) % m
            r = fast_mod(a, m - 1, m)
            if r != 1:
                return False
    return True


# # 欧几里得算法
# def euclid(a, b):
#     """
#     :param a: 整数
#     :param b: 整数a > b >= 0
#     :return: a和b的最大公约数(a, b)
#     """
#     x = a
#     y = b
#     while y != 0:
#         r = x % y
#         x = y
#         y = r
#     return x


# e的产生, 1 < e < phi_n, gcd(phi_n, e) = 1
def e_gen(phi_n):
    while True:
        e = random.randint(2, phi_n)
        # if euclid(e, phi_n) == 1:
        if ext_euclid(phi_n, e)[0] == 1:
            return e


# 扩展欧几里得算法
def ext_euclid(a, b):
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


# 模重复平方法
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
    e, n = pub_key
    cipher_text = fast_mod(plain_text, e, n)
    return cipher_text


# 解密
def decrypt(cipher_text, pri_key):
    d, n = pri_key
    plain_text = fast_mod(cipher_text, d, n)
    return plain_text


if __name__ == '__main__':
    pub, pri = key_gen()
    print('公钥是:', pub)
    plain = int(input('请输入明文m < n\n> '))
    cipher = encrypt(plain, pub)
    print('密文c = ', cipher)
    plain = decrypt(cipher, pri)
    print('解密后的明文m = ', plain)
