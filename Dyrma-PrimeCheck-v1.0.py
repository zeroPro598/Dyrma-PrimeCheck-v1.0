import time

# Lista e numrave të thjeshtë për filtrim fillestar
SMALL_PRIMES = [
    2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71,
    73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151,
    157, 163, 167, 173, 179, 181, 191, 193, 197, 199
]

def check_small_primes(n):
    """ Kontrollon nëse n është pjesëtues me ndonjë prim të vogël. """
    for p in SMALL_PRIMES:
        if n == p:
            return True
        if n % p == 0:
            return False
    return True

def power_mod(base, exp, mod):
    """ Ekspontencim modular (baza^exp % mod) për testin Miller-Rabin """
    result = 1
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp //= 2
    return result

def miller_rabin(n):
    """ Testi Miller-Rabin për primalitetin e n """
    if n < 2:
        return False
    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1

    # Dëshmitarët standardë për testin Miller-Rabin deri në 64-bit
    witnesses = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    for a in witnesses:
        if a >= n:
            continue
        x = power_mod(a, d, n)
        if x == 1 or x == n - 1:
            continue
        composite = True
        for _ in range(s - 1):
            x = power_mod(x, 2, n)
            if x == n - 1:
                composite = False
                break
        if composite:
            return False
    return True

def is_prime(n):
    """ Kombinon filtrimin me primët e vegjël dhe testin Miller-Rabin """
    if not check_small_primes(n):
        return False
    return miller_rabin(n)

def benchmark_prime_test(num):
    """ Teston primalitetin dhe mat kohën me precision të lartë """
    start = time.perf_counter_ns()  # Timer me precizion të lartë
    result = is_prime(num)
    end = time.perf_counter_ns()

    elapsed_time_ns = end - start  # Llogarit kohën e ekzekutimit
    print(f"{num} is prime? {result} | Time: {elapsed_time_ns} ns")

# Lista e numrave për testim
test_numbers = [
    99999999999999997,      # Prime
    1000000000000000003,    # Prime
    12345678910987654321,   # Composite
    9223372036854775783     # Prime
]

# Ekzekutimi i testimeve
for num in test_numbers:
    benchmark_prime_test(num)
