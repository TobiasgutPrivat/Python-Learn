n = 2

primes: list = []

while True:
    isPrime = True

    for prime in primes:
        if n % prime == 0:
            isPrime = False
            break

    if isPrime:
        primes.append(n)

    if n % 1000 == 0:
        print(n,"primes:",len(primes))

    n += 1