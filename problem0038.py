# www.github.com/GiacomoPinardi/project-euler

# Take the number 192 and multiply it by each of 1, 2, and 3:

#    192 x 1 = 192
#    192 x 2 = 384
#    192 x 3 = 576

# By concatenating each product we get the 1 to 9 pandigital, 192384576.
# We will call 192384576 the concatenated product of 192 and (1,2,3).

# The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5,
# giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

# What is the largest 1 to 9 pandigital 9-digit number that can be formed
# as the concatenated product of an integer with (1,2, ... , n) where n > 1?

def isPandigital (n):
    if len(n) != 9:
        return False

    for i in range(1, 10):
        if n.find(str(i)) == -1:
            return False

    return True

# Main

result = 0

for i in range(1, 10000):
    product = ""
    for j in range(1, int(9/len(str(i)))+2):
        if len(product) == 9 and isPandigital(product):
            print product
            result = max(result, product)
            break
        else:
            product += str(i*j)        

print result

#