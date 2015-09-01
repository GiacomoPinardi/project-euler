# www.github.com/GiacomoPinardi/project-euler

# The following iterative sequence is defined for the set of positive integers:
#  n -> n/2 (n is even)
#  n -> 3n + 1 (n is odd)
# Using the rule above and starting with 13, we generate the following sequence:
# 13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
# Which starting number, under one million, produces the longest chain?
# NOTE: Once the chain starts the terms are allowed to go above one million.

# Main


num = 0
maxLength = 0
result = 0

dictionary = {}

while num < 1000000:
    num += 1
    k = num
    i = 0
    while k > 1:
        if k in dictionary:
            i += dictionary[k]
            break

        i += 1
        if k%2 == 0:
            k /= 2
        else:
            k = k*3 + 1

    if not (num in dictionary):
        dictionary[num] = i

    if maxLength < i:
        maxLength = i
        result = num

print result

#
