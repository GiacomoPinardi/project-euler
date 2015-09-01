# www.github.com/GiacomoPinardi/project-euler

# You are given the following information, but you may prefer to do some research for yourself.

#     - 1 Jan 1900 was a Monday.
#     - Thirty days has September,
#    April, June and November.
#    All the rest have thirty-one,
#    Saving February alone,
#    Which has twenty-eight, rain or shine.
#    And on leap years, twenty-nine.
#     - A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

def isLeap (y):
	if y%400 == 0:
		return True
	elif y%100 == 0:
		return False
	elif y%4 == 0:
		return True
	else:
		return False

# Main

m = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

day = 1
month = 1
year = 1901

dayCount = 0

result = 0

while day != 1 or month != 1 or year != 2001:
	if dayCount%7 == 0 and day == 1:
		result += 1

	dayCount += 1

	if month == 12 and day == m[12]:
		year += 1
		month = 1
		day = 1
	elif month == 2 and day == 28 and isLeap(year):
		day += 1
	elif day >= m[month]:
		month += 1
		day = 1
	else:
		day += 1

print result

#
