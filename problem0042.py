# www.github.com/GiacomoPinardi/project-euler

# The nth term of the sequence of triangle numbers is given by, tn = (1/2)n(n+1)
# so the first ten triangle numbers are:

# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

# By converting each letter in a word to a number corresponding to its alphabetical
# position and adding these values we form a word value.
# For example, the word value for SKY is 19 + 11 + 25 = 55 = t10.
# If the word value is a triangle number then we shall call the word a triangle word.

# Using words.txt (right click and 'Save Link/Target As...'), a 16K text file
# containing nearly two-thousand common English words, how many are triangle words?

def readInput ():
    data = []
    f = file("input0042.txt", "r")
    for line in f:
        tmp = line.split(",")
        for s in tmp:
            s = s[1:len(s)-1]
            data.append(s.lower())

    return data

def generateTriangles():
    tri = []
    for i in range(1, 33):
        tri.append(int(i*(i+1)/2))

    return tri

# Main

words = readInput()
triangles = generateTriangles()
dictionary = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8, 'i':9, 'j':10, 'k':11, 'l':12, 'm':13, 'n':14, 'o':15, 'p':16, 'q':17, 'r':18, 's':19, 't':20, 'u':21, 'v':22, 'w':23, 'x':24, 'y':25, 'z':26}

result = 0

for word in words:
    s = 0
    for letter in word:
        s += dictionary[letter]

    if s in triangles:
        result += 1

print result