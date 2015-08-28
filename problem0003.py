# www.github.com/GiacomoPinardi/project-euler

# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

from math import sqrt

# Main

n = 600851475143
f_max = 1

i = 2

while n != 1 or i < int(sqrt(n))+1:
    if n%i == 0:
        f_max = max(f_max, i)
        n /= i
        i = 1
        
    i += 1

print f_max

#
