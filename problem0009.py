# www.github.com/GiacomoPinardi/project-euler

# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which, a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

def areOK (n1, n2):
    # must be coprime and n1-n2 odd
    while n2 != 0:
        n1, n2 = n2, n1%n2

    return n1 == 1 and (n1-n2)%2 == 1

# Main

n = 0

while n <= 32:
    n += 1
    m = 0
    while m <= 32:
        m += 1
        if areOK(m, n) and m != n:
            a = max(m,n)**2 - min(m,n)**2
            b = 2*m*n
            c = m**2 + n**2
            k = 0
            while (a+b+c)*k <= 1000:
                k += 1
                if (k*(a+b+c) == 1000):
                    x = sorted([k*a, k*b, k*c])
                    if x[0]**2 + x[1]**2 == x[2]**2:
                        print a*b*c*k**3

#
