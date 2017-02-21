# www.github.com/GiacomoPinardi/project-euler

# The prime 41, can be written as the sum of six consecutive primes:
# 41 = 2 + 3 + 5 + 7 + 11 + 13

# This is the longest sum of consecutive primes that adds to a prime below one-hundred.
# The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.
# Which prime, below one-million, can be written as the sum of the most consecutive primes?

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

def primeConsec (x, y):
    tot = 0
    for i in xrange(x, y):
        tot += primesList[i]

    return tot

# Main

primesErat = siege(1000000)
primesList = [x for x in xrange(0, len(primesErat)) if primesErat[x]]

result = 0
chain = 0

for i in xrange(0, 78498):
    for j in xrange(i, 78498):
        num = primeConsec(i, j)
        if num < 1000000 and primesErat[num]:
            if chain < j-i:
                result = num
                chain = j-i
        elif num > 1000000:
            break

print result