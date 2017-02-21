# www.github.com/GiacomoPinardi/project-euler

# There are exactly ten ways of selecting three from five, 12345:
# 123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

# In combinatorics, we use the notation, 5C3 = 10. In general,

# C(n, r) = (n!)/(r!(n-r)!)	, where r <= n, n! = nx(n-1)x...x3x2x1, and 0! = 1.

# It is not until n = 23, that a value exceeds one-million: C(23, 10) = 1144066.

# How many, not necessarily distinct, values of C(n, r), for 1 <= n <= 100, are greater than one-million?

def factorial (n):
	if n == 0 or n == 1:
		return 1
	else:
		return n * factorial(n-1)

def C(n, r):
	return factorial(n)/(factorial(r)*factorial(n-r))

# Main

result = 0

for n in xrange (1, 101):
	for r in xrange(1, n+1):
		if C(n, r) > 1000000:
			result += 1

print result