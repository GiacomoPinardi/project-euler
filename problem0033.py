# www.github.com/GiacomoPinardi/project-euler

# The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting
# to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

# We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

# There are exactly four non-trivial examples of this type of fraction,
# less than one in value, and containing two digits in the numerator and denominator.

# If the product of these four fractions is given in its lowest common terms,
# find the value of the denominator.

from math import sqrt

def good (n):
    if (n.find("0") == -1) and (n[0] != n[1]):
        return True
    
    return False

def check (n, d):
    a = float.hex(float(n)/float(d))
    for i in range(1, 10):
        num = str(n)
        denum = str(d)
        idx_num = num.find(str(i))
        idx_denum = denum.find(str(i))
        if idx_num != -1 and idx_denum != -1:
            num = num[:idx_num] + num[idx_num+1:]
            denum = denum[:idx_denum] + denum[idx_denum+1:]
            num = float(num)
            denum = float(denum)            
            if float.hex(num/denum) == a:
                return True

    return False

def simplify (array):
    x = 1
    y = 1
    for n in array:
        x *= n[0]
        y *= n[1]

    never = False

    while not never:
        never = True
        for i in range(2, int(sqrt(max(x, y)))):            
            if x%i == 0 and y%i == 0:
                x /= i
                y /= i
                never = False
                break

    return y

# Main

result = []

for i in range(12, 100):
    if good(str(i)):
        for j in range(i+1, 100):
            if good(str(j)):
                if check(i, j):
                    result.append([i, j])

print simplify(result)

#