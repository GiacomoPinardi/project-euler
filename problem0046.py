# www.github.com/GiacomoPinardi/project-euler

# It was proposed by Christian Goldbach that every odd composite
# number can be written as the sum of a prime and twice a square.

# 9 = 7 + 2x1^2
# 15 = 7 + 2x2^2
# 21 = 3 + 2x3^2
# 25 = 7 + 2x3^2
# 27 = 19 + 2x2^2
# 33 = 31 + 2x1^2

# It turns out that the conjecture was false.

# What is the smallest odd composite that cannot be written as the sum
# of a prime and twice a square?

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

def generateOnlyPrimes (prim):
    op = []
    for i in range(len(prim)):
        if prim[i]:
            op.append(i)

    return op

def isConjectureApplicable (n, op):
    i = 0
    while op[i] < n:
        x = op[i]
        j = 1
        while x+(2*(j**2)) <= n:
            if x+(2*(j**2)) == n:
                return True

            j += 1

        i += 1

    return False

# Main

result = 0
maxNum = 10000
primes = generatePrimes(maxNum)
onlyPrimes = generateOnlyPrimes(primes)


for i in range(9, maxNum, 2):
    if not primes[i]:
        if not isConjectureApplicable(i, onlyPrimes):
            result = i
            break

print result
