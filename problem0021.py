# www.github.com/GiacomoPinardi/project-euler

# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a != b,
# then a and b are an amicable pair and each of a and b are called amicable numbers.
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110;
# therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
# Evaluate the sum of all the amicable numbers under 10000.

from math import sqrt

def divSum (n):    
    if n in divisorsSum:
        return divisorsSum[n]
    else:
        # between divisors, n is excluded
        s = - n
        d = 0
        while d < int(sqrt(n))+1:
            d += 1
            if n%d == 0:
                s += d
                s += n/d

        divisorsSum[n] = s
        return s
        
# Main

result = 0

divisorsSum = {}

for j in range(10000):
    x = divSum(j)
    for k in range(10000):
        if j != k and x == k and divSum(k) == j:
            result += j + k

print result/2

#
