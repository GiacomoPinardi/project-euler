# www.github.com/GiacomoPinardi/project-euler

# The first two consecutive numbers to have two distinct prime factors are:

# 14 = 2 x 7
# 15 = 3 x 5

# The first three consecutive numbers to have three distinct prime factors are:

# 644 = 2^2 x 7 x 23
# 645 = 3 x 5 x 43
# 646 = 2 x 17 x 19.

# Find the first four consecutive integers to have four distinct prime factors.
# What is the first of these numbers?

from math import sqrt
import numpy

def generatePrimes (m):
    primes = numpy.ones((m), dtype=bool)

    for i in range(2, int(sqrt(len(primes)-2)+1)):
        if primes[i]:
            for j in range(i**2, len(primes), i):
                if primes[j]:
                    primes[j] = False

    primes[0] = False
    primes[1] = False
    return primes

def getPrimesFactor (n):
    factors = []
    while n != 1:
        for p in primesList:
            if n % p == 0:
                if p not in factors:
                    factors.append(p)
                n /= p
                break

    return factors

# Main

primesErat = generatePrimes(1000000)
primesList = [x for x in xrange(len(primesErat)) if primesErat[x]]

n = 1
count = 0

while count < 4:
    if len(getPrimesFactor(n)) == 4:
        count += 1
    else:
        count = 0

    n += 1

print n - 4
