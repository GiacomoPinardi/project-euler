# www.github.com/GiacomoPinardi/project-euler

# The number, 1406357289, is a 0 to 9 pandigital number because it is
# made up of each of the digits 0 to 9 in some order,
# but it also has a rather interesting sub-string divisibility property.

# Let d(1) be the 1st digit, d(2) be the 2nd digit, and so on. In this way, we note the following:

#    d(2)d(3)d(4)=406 is divisible by 2
#    d(3)d(4)d(5)=063 is divisible by 3
#    d(4)d(5)d(6)=635 is divisible by 5
#    d(5)d(6)d(7)=357 is divisible by 7
#    d(6)d(7)d(8)=572 is divisible by 11
#    d(7)d(8)d(9)=728 is divisible by 13
#    d(8)d(9)d(10)=289 is divisible by 17

# Find the sum of all 0 to 9 pandigital numbers with this property.

def getPermutation(n):
    if len(n) == 1:
        return str(n[0])
    else:
        perm = getPermutation(n[:len(n)-1])
        result = []

        for p in perm:
            new = str(n[len(n)-1])
            for i in range(len(p)+1):
                result.append(p[:i] + new + p[i:])

        return result

# Main

result = 0
digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
divisors = [2, 3, 5, 7, 11, 13, 17]

permutations = getPermutation(digits)

for perm in permutations:
    div = True
    for i in range(7):
        if not int(perm[i+1:i+4])%divisors[i] == 0:
            div = False

    if div:
        print perm
        result += int(perm)

print result