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

def generateOnlyPrimes (prim):
    op = []
    for i in range(len(prim)):
        if prim[i]:
            op.append(i)

    return op

def getPrimesFactor (n, onlyPrimes):
    fact = []
    if n in dictFactors:
        fact += dictFactors[n]
    else:
        if n in onlyPrimes:
            fact.append(n)
        else:
            for p in onlyPrimes:
                if n%p == 0:
                    fact.append(p)
                    fact += getPrimesFactor(n/p, onlyPrimes)
                    break

    return fact

def getZippedFactors (factors):
    d = {}
    zF = []
    for f in factors:
        if f in d:
            d[f] += 1
        else:
            d[f] = 1

    for key in d:
        zF.append(key**d[key])

    return zF

def haveDistinctFactors (arrays):
    total = []
    for a in arrays:
        total += a

    return len(total) == len(set(total))

# Main

result = 0
maxNum = 1000000
primes = generatePrimes(maxNum)
onlyPrimes = generateOnlyPrimes(primes)

dictFactors = {}

distinct = 4

oldValues = []
i = 2

while i < maxNum:
    if i%10000 == 0:
        print i
        
    facts = getPrimesFactor(i, onlyPrimes)
    dictFactors[i] = facts
    zFacts = getZippedFactors(facts)
    if len(zFacts) == distinct:
        oldValues.append(zFacts)
        if len(oldValues) > distinct:
            del oldValues[0]

        if len(oldValues) == distinct and haveDistinctFactors(oldValues):
            result = i
            break

    else:
        oldValues = []

    i += 1


print result-distinct+1
