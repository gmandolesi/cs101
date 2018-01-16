# Define a daysBetweenDates procedure that would produce the
# correct output if there was a correct nextDay procedure.
#
# Note that this will NOT produce correct outputs yet, since
# our nextDay procedure assumes all months have 30 days
# (hence a year is 360 days, instead of 365).
# 

def isLeapYear(year):
	if year % 400 == 0:
		return True
	if year % 100 == 0:
		return False
	if year % 4 == 0:
		return True
	return False


def daysInMonth(year, month):
	if (month%2 == 1):
		if (month < 8):
			return 31
		return 30
	if month > 7:
		return 31
	if month != 2:
		return 30
	if isLeapYear(year):
		return 29
	return 28

def nextDay(year, month, day):
    """Simple version: assume every month has 30 days"""
    if day < daysInMonth(year, month):
        return year, month, day + 1
    if month == 12:
        return year + 1, 1, 1
    return year, month + 1, 1
        
def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar, and the first date is not after
       the second."""
    days = 0

	#check consistency of input data before starting
    assert ((year2*10000 + month2*100 + day2) > (year1*10000 + month1*100 + day1))
 
    while ((year2*10000 + month2*100 + day2) > (year1*10000 + month1*100 + day1)):
        year1, month1, day1 = nextDay(year1, month1, day1)
        days = days+1
    return days

def test():
    test_cases = [((2012,9,30,2012,10,30),30), 
                  ((2012,1,1,2013,1,1),360),
                  ((2012,9,1,2012,9,4),3),
                  ((2013,1,1,1999,12,31), "AssertionError")]
    
    for (args, answer) in test_cases:
        try:
            result = daysBetweenDates(*args)
            if result != answer:
                print "Test with data:", args, "failed"
            else:
                print "Test case passed!"
        except AssertionError:
            if answer == "AssertionError":
                print "Nice job! Test case {0} correctly raises AssertionError!\n".format(args)
            else:
                print "Check your work! Test case {0} should not raise AssertionError!\n".format(args)  

test()
    

