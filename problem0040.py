# www.github.com/GiacomoPinardi/project-euler

# An irrational decimal fraction is created by concatenating the positive integers:

# 0.12345678910(1)112131415161718192021...

# It can be seen that the 12th digit of the fractional part is 1.
# If d(n) represents the nth digit of the fractional part, find the value of the following expression.

# d(1) x d(10) x d(100) x d(1000) x d(10000) x d(100000) x d(1000000)


# Main

result = 1

s = ""

for i in range(1, 1000001):
	s += str(i)

result = int(s[0]) * int(s[9]) * int(s[99]) * int(s[999]) * int(s[9999]) * int(s[99999]) * int(s[999999])

print result

#