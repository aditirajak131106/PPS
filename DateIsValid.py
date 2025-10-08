year = int(input("year: "))
month = int(input("month: "))
day = int(input("day: "))
leap_year = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
days_in_month = [31,29 if leap_year else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if 1 <= month <= 12 and 1 <= day <= days_in_month[month-1]:
	day +=1
	if day > days_in_month[month-1]:
		day = 1
		month += 1
		if month > 12:
			month = 1
			year += 1
	print("valid")
	print(f"incremented date: {year}-{month:02d}-{day:02d}")
else:
	print("invalid")
