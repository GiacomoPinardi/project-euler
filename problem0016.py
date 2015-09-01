# www.github.com/GiacomoPinardi/project-euler

# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
# What is the sum of the digits of the number 2^1000?


# Main

num = str(2**1000)
result = 0

for n in num:
    result += int(n)

print result

#
