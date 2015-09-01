# www.github.com/GiacomoPinardi/project-euler

# Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names,
# begin by sorting it into alphabetical order. Then working out the alphabetical value for each name,
# multiply this value by its alphabetical position in the list to obtain a name score.
# For example, when the list is sorted into alphabetical order,
# COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list.
# So, COLIN would obtain a score of 938 x 53 = 49714.
# What is the total of all the name scores in the file?


def readInput ():
    return open('input0022.txt').read().split(",")

# Main

array = sorted(readInput())

result = 0

for i in range(len(array)):
	value = 0
	for c in array[i].lower():
		value += ord(c) - 96
	result += value * (i+1)

print result

#