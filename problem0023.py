# www.github.com/GiacomoPinardi/project-euler

# A perfect number is a number for which the sum of its proper divisors is exactly equal to the number.
# For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28,
# which means that 28 is a perfect number.
# A number n is called deficient if the sum of its proper divisors is less than n
# and it is called abundant if this sum exceeds n.
# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16,
# the smallest number that can be written as the sum of two abundant numbers is 24.
# By mathematical analysis, it can be shown that all integers greater than 28123
# can be written as the sum of two abundant numbers.
# However, this upper limit cannot be reduced any further by analysis even though
# it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.
# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

from math import sqrt

def isAbdundant (n):
    d = 0
    divisors = []

    while d < int(sqrt(n)):
        d += 1
        if n%d == 0 and d not in divisors:
            divisors.append(d)
            x = n/d
            if d != 1 and x not in divisors:
                divisors.append(x)

    return sum(divisors) > n

# Main

result = 0
n = 0

abdundant = []

while n <= 28123:
    n += 1
    print n
    if isAbdundant(n):
        abdundant.append(n)

    isSum = False
    for a in abdundant:
        if (n-a) in abdundant:
            isSum = True
            break

    if not isSum:
        result += n

print result

#