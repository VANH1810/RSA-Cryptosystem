import math

def aks(n):
    if is_power(n):
        return False

    r = find_r(n)

    if r is None:
        return True
    for a in range(1, r + 1):
        if math.gcd(a, n) > 1:
            return False
        
    for a in range(2, int(math.sqrt(r)) + 1):
        x = pow(a,n,n)
        y = pow((x-a),n,n)
        if x!=y:
            return False

    return True


def is_power(n):
    if n <= 1:
        return False

    max_exponent = int(math.log2(n))

    for b in range(2, int(math.sqrt(n)) + 1):
        i = 2
        while pow(b, i) <= n:
            if pow(b, i) == n:
                return True
            i += 1
        if i > max_exponent:
            break

    return False


def find_r1(n):
    max_r = int(math.log2(n) ** 2)
    primes = sieve_of_eratosthenes(max_r)

    for r in primes:
        if r > n:
            return None
        if pow(n, n, r) != n % r:
            return r
def find_r(n):
    r = 2
    while r <= int(math.log2(n) ** 2):
        if math.gcd(n, r) != 1:
            return r
        else:
            r += 1
    return r


def sieve_of_eratosthenes(n):
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False

    p = 2

    while p * p <= n:
        if primes[p]:
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1

    return [p for p in range(n + 1) if primes[p]]

n = 3

if aks(n):
    print(n, "is prime")
else: 
    print(n, "is not prime")

print(find_r(n))
print(find_r1(n))
