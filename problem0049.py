# www.github.com/GiacomoPinardi/project-euler

# The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330,
# is unusual in two ways: (i) each of the three terms are prime, and,
# (ii) each of the 4-digit numbers are permutations of one another.

# There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes,
# exhibiting this property, but there is one other 4-digit increasing sequence.

# What 12-digit number do you form by concatenating the three terms in this sequence?

def siege (n):
    num = [1]*n
    num[0] = 0
    num[1] = 0

    for i in xrange(int(n**0.5)+1):
        if num[i]:
            j = 0
            while i**2+j*i < n:            
                num[i**2+j*i] = 0
                j += 1

    return num

# Main

primes = siege(10000)

for i in xrange(1000, 10000):
	if primes[i]:
		for inc in xrange(1, 4500):
			if i+2*inc <= 10000 and primes[i+inc] and primes[i+2*inc]:
				if sorted(str(i)) == sorted(str(i+inc)) and sorted(str(i)) == sorted(str(i+2*inc)):
					print str(i) + " - " + str(i+inc) + " - " + str(i+2*inc)