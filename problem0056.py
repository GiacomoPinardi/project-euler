# www.github.com/GiacomoPinardi/project-euler

# A googol (10^100) is a massive number: one followed by one-hundred zeros;
# 100^100 is almost unimaginably large: one followed by two-hundred zeros.
# Despite their size, the sum of the digits in each number is only 1.

# Considering natural numbers of the form, ab, where a, b < 100, what is the maximum digital sum?

def sumDigit(n):
    tot = 0
    for digit in str(n):
        tot += int(digit)

    return tot

# Main

result = 0

for a in xrange(1, 100):
    for b in xrange(1, 100):
        actual = sumDigit(a**b)
        if actual > result:
            result = actual

print result