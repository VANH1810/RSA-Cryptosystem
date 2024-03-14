import random

def fast_power(a, d, n):
    result = 1
    while d > 0:
        if d % 2 == 1:
            result = (result * a) % n
        a = (a**2) % n
        d //= 2
    return result

def miller_rabin(n, k=20):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False

    def check(a, s, d, n):
        x = fast_power(a, d, n)
        if x == 1:
            return True
        for _ in range(s - 1):
            if x == n - 1:
                return True
            x = fast_power(x, 2, n)
        return x == n - 1

    s = 0
    d = n - 1
    while d % 2 == 0:
        d //= 2
        s += 1

    for _ in range(k):
        a = random.randint(2, n - 2)
        if not check(a, s, d, n):
            return False

    return True

def generate_prime(bits):
    while True:
        p = random.getrandbits(bits)
        if p % 2 == 0:
            p += 1
        if miller_rabin(p):
            return p

def generate_pq(bits):
    p = generate_prime(bits)
    q = generate_prime(bits)
    while p == q:
        q = generate_prime(bits)
    return p, q

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def generate_e(phi_n, bits):
    while True:
        e = random.randint(2**(bits-1), 2**bits - 1)
        if gcd(e, phi_n) == 1:
            return e
        
def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    else:
        d, x, y = extended_gcd(b, a % b)
        return d, y, x - y * (a // b)

def mod_inverse(e, phi_n):
    gcd, x, y = extended_gcd(e, phi_n)
    if gcd != 1:
        raise ValueError("e doesn't have inverse module phi_n")
    else:
        return x % phi_n


#Generate key p, q, e, n, d:
bits_pq = 80
p, q = generate_pq(bits_pq)
print("p:", p)
print("q:", q)


phi_n = (p - 1) * (q - 1)
bits_e = 50
e = generate_e(phi_n, bits_e)
print("e:", e)

n = (p * q)
print("n:", n)

d = mod_inverse(e, phi_n)
print("d:", d)

