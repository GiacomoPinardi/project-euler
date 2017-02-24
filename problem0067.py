# www.github.com/GiacomoPinardi/project-euler

# By starting at the top of the triangle below and moving to adjacent numbers on the row below,
# the maximum total from top to bottom is 23.

# 3
# 7 4
# 2 4 6
# 8 5 9 3

# That is, 3 + 7 + 4 + 9 = 23.

# Find the maximum total from top to bottom in triangle.txt
# (right click and 'Save Link/Target As...'), a 15K text file containing a
# triangle with one-hundred rows.

# NOTE: This is a much more difficult version of Problem 18. It is not possible to try every
# route to solve this problem, as there are 299 altogether! If you could check one trillion
# (1012) routes every second it would take over twenty billion years to check them all.
# There is an efficient algorithm to solve it. ;o)

def readInput ():
    raw = open('input0067.txt').read().split("\n")
    array = []

    for e in raw:
        array.append([int(x) for x in e.split(' ')])

    return array

# Main

array = readInput()

for i in range(1, len(array)):
	for k in range(len(array[i])):
		if k == 0:
			array[i][k] += array[i-1][k]
		elif k == len(array[i])-1:
			array[i][k] += array[i-1][k-1]
		else:
			array[i][k] += max(array[i-1][k], array[i-1][k-1])

print max(array[len(array)-1])

#
