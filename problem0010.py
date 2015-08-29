# www.github.com/GiacomoPinardi/project-euler

# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

from math import sqrt

def isPrime (n):
    for i in range(2, int(sqrt(n))+1):
        if n%i == 0:
            return False
    return True

# Main

result = 2
num = 1

while num < 2000000:
    num += 2
    if isPrime(num):
        result += num

print result

#
