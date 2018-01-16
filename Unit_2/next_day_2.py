def next_Day(year, month, day):
	if day < 30:
		return year, month, day+1
	if month < 12:
		return year, month+1, day
	return year+1,1,1
