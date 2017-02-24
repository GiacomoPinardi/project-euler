# www.github.com/GiacomoPinardi/project-euler

# Each character on a computer is assigned a unique code and the preferred standard
# is ASCII (American Standard Code for Information Interchange).
# For example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.

# A modern encryption method is to take a text file, convert the bytes to ASCII,
# then XOR each byte with a given value, taken from a secret key.
# The advantage with the XOR function is that using the same encryption key on the cipher text,
# restores the plain text; for example, 65 XOR 42 = 107, then 107 XOR 42 = 65.

# For unbreakable encryption, the key is the same length as the plain text message,
# and the key is made up of random bytes. The user would keep the encrypted message and
# the encryption key in different locations, and without both "halves", it is
# impossible to decrypt the message.

# Unfortunately, this method is impractical for most users, so the modified method is to
# use a password as a key. If the password is shorter than the message, which is likely,
# the key is repeated cyclically throughout the message. The balance for this method is
# using a sufficiently long password key for security, but short enough to be memorable.

# Your task has been made easy, as the encryption key consists of three lower case characters.
# Using cipher.txt (right click and 'Save Link/Target As...'), a file containing the encrypted
# ASCII codes, and the knowledge that the plain text must contain common English words, decrypt
# the message and find the sum of the ASCII values in the original text.

def readInput ():
    inp = open("input0059.txt", "r")
    nums = inp.read().split(',')

    return nums

def XOR (x, y):
    return str(int(x != y))

def XORChar (a, b):
    result = ""
    aBit = bin(ord(a))[2:].zfill(8)
    bBit = bin(ord(b))[2:].zfill(8)

    for i in xrange(len(aBit)):
        result += XOR(aBit[i], bBit[i])

    return chr(int(result, 2))

# Main

result = 0

encryptedNum = readInput()
encryptedChar = ""

for num in encryptedNum:
    encryptedChar += chr(int(num))

for a in xrange(97, 123):
    for b in xrange(97, 123):
        for c in xrange(97, 123):

            key = chr(a) + chr(b) + chr(c)

            keyLong = key * (len(encryptedChar) / len(key) + 1)

            decryptedChar = ""

            for j in xrange(len(encryptedChar)):
                decryptedChar += XORChar(encryptedChar[j], keyLong[j])

            if "because" in decryptedChar:
                for letter in decryptedChar:
                    result += ord(letter)

                print result
