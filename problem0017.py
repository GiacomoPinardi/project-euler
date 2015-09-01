# www.github.com/GiacomoPinardi/project-euler

# If the numbers 1 to 5 are written out in words: one, two, three, four, five,
# then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words,
# how many letters would be used?
# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters
# and 115 (one hundred and fifteen) contains 20 letters.
# The use of "and" when writing out numbers is in compliance with British usage.

def split (n):
    array = []

    p = 0
    while n != 0:
        k = n%10
        array.insert(0, k*(10**p))
        n = (n-k)/10
        p += 1

    return merge(array)

def merge (array):
    try:
        idx = array.index(10)
        array.insert(idx, array[idx] + array[idx+1])
        del array[len(array)-1]
        del array[len(array)-1]
    except ValueError:
        pass

    return array

# Main

d = {1: 3, 2: 3, 3: 5, 4: 4, 5: 4, 6: 3, 7: 5, 8: 5, 9: 4, 10: 3, 11: 6, 12: 6, 13: 8, 14: 8, 15: 7, 16: 7, 17: 9, 18: 8, 19: 8, 20: 6, 30: 6, 40: 5, 50: 5, 60: 5, 70: 7, 80: 6, 90: 6, 100: 7, 1000: 11}

result = 0

for i in range(1, 1001):
    array = split(i)

    print array

    r = 0
    for e in array:
        if e != 0:
            if e%100 == 0 and e != 1000:
                r += d[e/100] + d[100]
                if i%100 != 0:
                    r += 3
            else:
                r += d[e]

    result += r
    print str(i) + ": " + str(r)

print result

#
