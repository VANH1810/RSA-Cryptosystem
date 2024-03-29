import random
import aks
def fast_power(a, d, n):
    result = 1
    while d > 0:
        if d % 2 == 1:
            result = (result * a) % n
        a = (a**2) % n
        d //= 2
    return result

# Pre generated primes
first_primes_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
                     31, 37, 41, 43, 47, 53, 59, 61, 67,
                     71, 73, 79, 83, 89, 97, 101, 103,
                     107, 109, 113, 127, 131, 137, 139,
                     149, 151, 157, 163, 167, 173, 179,
                     181, 191, 193, 197, 199, 211, 223,
                     227, 229, 233, 239, 241, 251, 257,
                     263, 269, 271, 277, 281, 283, 293,
                     307, 311, 313, 317, 331, 337, 347, 349]
def LowLevelPrimeCheck(n):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False
    for divisor in first_primes_list:
        if n % divisor == 0 and divisor**2 <= n:
            return False
    return True
def Miller_Rabin_Prime_Check(n, k=20):
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
        p = random.randint(2**(bits-1), 2**bits - 1)
        if p % 2 == 0:
            p += 1
        if LowLevelPrimeCheck(p):
            if Miller_Rabin_Prime_Check(p):
                if aks.aks(p):
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
bits_pq = 1024
p, q = generate_pq(bits_pq)
print("p:", p)
print("q:", q)


phi_n = (p - 1) * (q - 1)
bits_e = bits_pq / 2
e = generate_e(phi_n, bits_e)
print("e:", e)

n = (p * q)
print("n:", n)

d = mod_inverse(e, phi_n)
print("d:", d)

with open("public_key.txt", 'w') as file:
    file.write(str(e) + "\n")
    file.write(str(n))
print("Public key to", "public_key.txt")

with open("private_key.txt", 'w') as file:
    file.write(str(d) + "\n")
    file.write(str(n) + "\n")
print("Private key to", "private_key.txt")