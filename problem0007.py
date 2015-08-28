# www.github.com/GiacomoPinardi/project-euler

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?

from math import sqrt

def isPrime (n):
    for i in range(2, int(sqrt(n))+1):
        if n%i == 0:
            return False
    return True

# Main

pth = 1
num = 1

while pth < 10001:
    num += 2
    if isPrime(num):
        pth += 1

print num

#
