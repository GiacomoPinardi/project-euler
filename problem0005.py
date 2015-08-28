# www.github.com/GiacomoPinardi/project-euler

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def gcd (n1, n2):
    while n2 != 0:
        n1, n2 = n2, n1%n2

    return n1

def lcm (n1, n2):
    return (n1*n2)/gcd(n1, n2)

# Main

num = [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

result = 1

for i in range(len(num)):
    result = lcm(result, num[i])

print result

#
