# www.github.com/GiacomoPinardi/project-euler

# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

def isPalindrome(n):
    num = str(n)

    for i in range(int(len(num)/2)):
        if num[i] != num[len(num)-(i+1)]:
            return False
    return True

# Main

found = 0

n1 = 999

while n1 > 1:
    n2 = 999
    while n2 > 1:
        if isPalindrome(n1*n2):
            found = max(found, n1*n2)
        n2 -= 1
    n1 -= 1

print found

#
