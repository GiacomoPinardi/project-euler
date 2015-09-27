# www.github.com/GiacomoPinardi/project-euler

# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once;
# for example, the 5-digit number, 15234, is 1 through 5 pandigital.

# The product 7254 is unusual, as the identity, 39 x 186 = 7254,
# containing multiplicand, multiplier, and product is 1 through 9 pandigital.

# Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
# HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.

def checkPandigitality (s) :
    r = False
    if len(s) == 9:
        r = True      
        for k in range(1, 10):
            if s.find(str(k)) == -1:
                return False

    return r

def duplicateNumbers (s) :
    s = sorted(s)
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            return True

    return False

# Main

result = []

l = 3000

for i in range(1, l):
    if not duplicateNumbers(str(i)):       
        for j in range(i+1, l):    
            s = str(i) + str(j) + str(i*j)
            if checkPandigitality(s):
                if not i*j in result:
                    result.append(i*j)

print sum(result)

#