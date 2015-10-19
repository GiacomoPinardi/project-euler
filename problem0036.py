# www.github.com/GiacomoPinardi/project-euler

# The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.
# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
# (Please note that the palindromic number, in either base, may not include leading zeros.)

def isPalindrome(n):
    num = str(n)

    for i in range(int(len(num)/2)):
        if num[i] != num[len(num)-(i+1)]:
            return False
    return True

# Main

result = 0

for i in range(1, 1000000):
    if isPalindrome(i) and isPalindrome(bin(i)[2:]):
        result += i

print result

#