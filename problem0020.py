# www.github.com/GiacomoPinardi/project-euler

# n! means n x (n - 1) x ... x 3 x 2 x 1
# For example, 10! = 10 x 9 x ... x 3 x 2 x 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
# Find the sum of the digits in the number 100!


# Main

num = 100
f = 1

result = 0

for i in range(1, num+1):
	f *= i

f = str(f)

for s in f:
	result += int(s)

print result

#
