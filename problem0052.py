# www.github.com/GiacomoPinardi/project-euler

# It can be seen that the number, 125874, and its double, 251748,
# contain exactly the same digits, but in a different order.

# Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.

# Main

result = 1

while not (sorted(str(result)) == sorted(str(2*result)) == sorted(str(3*result)) == sorted(str(4*result)) == sorted(str(5*result)) == sorted(str(6*result))):
    result += 1

print result