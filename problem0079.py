# www.github.com/GiacomoPinardi/project-euler

# A common security method used for online banking is to ask the user for three
# random characters from a passcode. For example, if the passcode was 531278,
# they may ask for the 2nd, 3rd, and 5th characters; the expected reply would be: 317.

# The text file, keylog.txt, contains fifty successful login attempts.

# Given that the three characters are always asked for in order, analyse the file so as
# to determine the shortest possible secret passcode of unknown length.

import itertools

def check (password):
	for key in keylog:
		if password.index(key%10) < password.index((key/10)%10) or password.index((key/10)%10) < password.index((key/100)%10):
			return False

	return True


# Main

result = ""

digits = [0, 1, 2, 3, 6, 7, 8, 9]

keylog = [319, 680, 180, 690, 129, 620, 762, 689, 762, 318, 368, 710, 720, 710, 629, 168, 160, 689, 716, 731, 736, 729, 316, 729, 729, 710, 769, 290, 719, 680, 318, 389, 162, 289, 162, 718, 729, 319, 790, 680, 890, 362, 319, 760, 316, 729, 380, 319, 728, 716]

passwords = list(itertools.permutations(digits))

for p in passwords:
	if check(p):
		result = ''.join(map(str, p))

print result

#
