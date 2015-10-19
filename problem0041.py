# www.github.com/GiacomoPinardi/project-euler

# We shall say that an n-digit number is pandigital if it makes use 
# of all the digits 1 to n exactly once. 
# For example, 2143 is a 4-digit pandigital and is also prime.

# What is the largest n-digit pandigital prime that exists?


from math import sqrt

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

def isPrime (n):
    for i in range(2, int(sqrt(n))+1):
        if n%i == 0:
            return False
    return True

# Main

result = 0

numbers = [1, 2, 3, 4, 5, 6, 7]

allPandigitals = sorted(getPermutation(numbers), reverse=True)

for n in allPandigitals:
    if isPrime(int(n)):
        result = n
        break

print result