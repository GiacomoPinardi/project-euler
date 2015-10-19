# www.github.com/GiacomoPinardi/project-euler

# The number 3797 has an interesting property.
# Being prime itself, it is possible to continuously remove digits from left to right,
# and remain prime at each stage: 3797, 797, 97, and 7.
# Similarly we can work from right to left: 3797, 379, 37, and 3.

# Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

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

def allPrimes (n):
    n = str(n)
    for i in range(1, len(n)):
        if not primes[int(n[i:])] or not primes[int(n[:i])]:
            return False

    return True

# Main

result = 0

l = 1000000
primes = generatePrimes(l)

for i in range(11, l, 2):
    if primes[i] and allPrimes(i):
        result += i

print result

#