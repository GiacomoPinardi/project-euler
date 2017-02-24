# www.github.com/GiacomoPinardi/project-euler

# The 5-digit number, 16807=7^5, is also a fifth power. Similarly, the 9-digit number,
# 134217728=8^9, is a ninth power.

# How many n-digit positive integers exist which are also an nth power?

# Main

result = 0

for a in xrange(1, 101):
    for b in xrange(1, 101):
        if len(str(a**b)) == b:
            result += 1

print result