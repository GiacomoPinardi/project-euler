# www.github.com/GiacomoPinardi/project-euler

# Starting in the top left corner of a 2x2 grid, and only being able to move to the right and down,
# there are exactly 6 routes to the bottom right corner.
# How many such routes are there through a 20x20 grid?

# Main

routes = 0
# l = 20 (Generate Memory Error)
l = 10

maximium = 2**(l*2)

for i in range(0, maximium):
    b = bin(i)[2:]
    z = "0" * (l*2-len(b))
    b = z+b

    if b.count('0') == b.count('1'):
        routes += 1

print routes

#
