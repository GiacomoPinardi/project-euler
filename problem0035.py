# www.github.com/GiacomoPinardi/project-euler

# The number, 197, is called a circular prime because
# all rotations of the digits: 197, 971, and 719, are themselves prime.

# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

# How many circular primes are there below one million?

from math import sqrt
import numpy

def encircle (n):
	array = []
	for i in range(len(n)):
		n = n[1:] + n[:1]
		array.append(int(n))

	return array

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

# Main

result = 0

primes = generatePrimes(1000000)

for i in range(2, 1000000):
	c = encircle(str(i))
	allPrimes = True
	for e in c:
		if not primes[e]:
			allPrimes = False

	if allPrimes:
		result += 1


print result

#