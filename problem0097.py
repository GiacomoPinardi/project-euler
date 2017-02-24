# www.github.com/GiacomoPinardi/project-euler

# The first known prime found to exceed one million digits was discovered in 1999,
# and is a Mersenne prime of the form 26972593-1; it contains exactly 2,098,960 digits.
# Subsequently other Mersenne primes, of the form 2p-1, have been found which contain more digits.

# However, in 2004 there was found a massive non-Mersenne prime which contains 2,357,207 digits: 28433x27830457+1.

# Find the last ten digits of this prime number.

# Main

num = 2

for i in xrange(2, 7830458):
	num *= 2
	num = num % 10000000000

num *= 28433
num += 1

print str(num)[-10:]

#
